# Node colors
BLACK = 0
RED = 1


class RedBlackNode:
    def __init__(self, key, content=None, color=RED, parent=None, left=None, right=None):
        self.key = key
        self.content = content
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color


class NullNodeError(Exception):
    pass


class InvalidInsertNodeError(Exception):
    pass


def _find_closest_ancestor_by_key(node, key):
    # have we found an exact match?
    if key == node.key:
        return node

    # go right if the search key is greater than this node's key, otherwise left
    if key > node.key and node.right is not None:
        return _find_closest_ancestor_by_key(node.right, key)
    elif node.left is not None:
        return _find_closest_ancestor_by_key(node.left, key)

    # we hit a dead end, so this is close enough
    return node


def _insert_at_node(node, key, content, color=RED):
    to_insert = RedBlackNode(key, content, color, parent=node)

    if key > node.key and node.right is None:
        node.right = to_insert
    elif node.left is None:
        node.left = to_insert
    else:
        raise InvalidInsertNodeError()

    # return the inserted node
    return to_insert


def _find_sibling(node):
    if node is None or node.parent is None:
        return None

    # return this node's sibling
    if node.parent.left == node:
        return node.parent.right
    return node.parent.left


def _get_node_color(node):
    if node is None:
        return BLACK
    return node.color


def _flip_color(node):
    if node is None:
        raise NullNodeError()

    if node.color == BLACK:
        node.color = RED
    else:
        node.color = BLACK


def _red_uncle_recolor(node):
    # flip our color and our sibling
    _flip_color(node)
    sibling = _find_sibling(node)
    if sibling is not None:
        _flip_color(sibling)

    # change parent color if a parent exists, if not, then we are done
    if node.parent is not None:
        _flip_color(node.parent)
    else:
        return

        # check if our uncle is red, if so, repeat this process
    if _get_node_color(_find_sibling(node.parent)) == RED:
        _red_uncle_recolor(node.parent)


def _left_rotation(node):
    #     parent            parent
    #       /  \    =>      /  \
    #    node   4          X    4
    #    /  \             /  \
    #   1    X          node  3
    #       / \          / \
    #      2   3        1   2
    parent = node.parent
    x = node.right

    # when node.right is None, a left rotation cannot be performed
    if x is None:
        raise NullNodeError()

    x_left = x.left

    # move x into position as a child of our parent
    # node is now unconnected
    if parent is not None:
        if parent.left == node:
            parent.left = x
        else:
            parent.right = x
    x.parent = parent

    # move node into position at x.left
    # the node originally at x.left is now unconnected
    x.left = node
    node.parent = x

    # move the node originally at x.left to node.right
    node.right = x_left
    if x_left is not None:
        x_left.parent = node


def _right_rotation(node):
    #      parent        parent
    #      /  \     =>    / \
    #    node    4       X   4
    #    /  \           /  \
    #   X    3         1   node
    #  / \                 /  \
    # 1   2               2    3
    parent = node.parent
    x = node.left

    # when node.left is None, a right rotation cannot be performed
    if x is None:
        raise NullNodeError()

    x_right = x.right

    # move x into position as a child of our parent
    # node is now unconnected
    if parent is not None:
        if parent.left == node:
            parent.left = x
        else:
            parent.right = x
    x.parent = parent

    # move node into position at x.right
    # the node originally at x.right is now unconnected
    x.right = node
    node.parent = x

    # move the node originally at x.right to node.right
    node.left = x_right
    if x_right is not None:
        x_right.parent = node


def _find_node_by_key(node, key):
    # if there is no root node, obviously the key is not findable
    if node is None:
        raise KeyError()

    # recurse into the tree to locate the key
    found = _find_closest_ancestor_by_key(node, key)

    # check if we found the actual node, or just a close match
    if found.key != key:
        raise KeyError()

    return found


def _copy_node(src, dest):
    dest.key = src.key
    dest.content = src.content


def _rebalance_double_black(node):
    # rebalancing is required when a leaf node is deleted that is not the root
    if node.parent is not None:
        sibling = _find_sibling(node)
        if _get_node_color(sibling) == BLACK:
            # Case 1a - sibling is black and one at least one child is red
            if _get_node_color(sibling.left) == RED or _get_node_color(sibling.right) == RED:
                raise Exception("Unimplimented")

            # Case1b - sibling is black and both children are black
            else:
                raise Exception("Unimplimented")

        # Case 1c - sibling is red
        else:
            raise Exception("Unimplimented")


def _replace_parent_with_child(child, parent):
    # if the two merging nodes are different colors, make the new node black
    # merge, and delete the old child
    if _get_node_color(parent) != _get_node_color(child):
        parent.color = BLACK
        _copy_node(child, parent)
        _delete_node(child)

    # the nodes are both BLACK, and must be rebalanced
    else:
        raise("Unimplimented")


def _delete_node(node):
    # non-existant nodes can't be deleted!
    if node is None:
        raise NullNodeError()

    parent = node.parent

    # Case 1 - leaf node
    if node.left is None and node.right is None:
        # deleting a leaf node causes a double-black condition
        # and needs rebalancing
        _rebalance_double_black(node)

        # remove the node
        if node.parent is not None:
            node.parent = None
            del node

    # left child exists
    elif node.left is not None:

        # Case 2a - left is an only child.
        if node.right is None:
            _replace_parent_with_child(node.left, node)

        # Case 3 - node has two children
        else:
            # find in-order sucessor of this node
            sucessor = node.right
            while sucessor.left is not None:
                sucessor = sucessor.left

            # if the in-order sucessor is also a child, use the defined process for that
            if sucessor == node.right:
                _replace_parent_with_child(sucessor, node)

            # copy the sucessor into node, and delete sucessor
            # (where sucessor is not a child of node)
            # (sucessor is also always a leaf or has only a right child)
            else:
                _copy_node(sucessor, node)
                _delete_node(sucessor)

    # Case 2b - right is an only child
    else:
        _replace_parent_with_child(node.right, node)


class RedBlackTree:
    def __init__(self):
        self.__root = None

    def insert(self, key, content=None):
        # special case, we are inserting the first node in the tree
        # this node starts off as black
        if self.__root is None:
            self.__root = RedBlackNode(key, content, BLACK)
            return

        parent = _find_closest_ancestor_by_key(self.__root, key)
        inserted = _insert_at_node(parent, key, content)

        # if our parent is black, then no change is needed
        if _get_node_color(parent) == BLACK:
            return

        if _get_node_color(_find_sibling(parent)) == RED:
            _red_uncle_recolor(parent)

        else:
            # determine this node and parent's position within their parents
            parent_left_of_grand = True
            if inserted.parent.parent.left != inserted.parent:
                parent_left_of_grand = False

            inserted_left_of_parent = True
            if inserted.parent.left != inserted:
                inserted_left_of_parent = False

            # Case 1 - left left
            if parent_left_of_grand and inserted_left_of_parent:
                _flip_color(inserted.parent.parent)
                _flip_color(inserted.parent)
                _right_rotation(inserted.parent.parent)

            # Case 2 - left right
            elif parent_left_of_grand and not inserted_left_of_parent:
                _flip_color(inserted.parent.parent)
                _flip_color(inserted)
                _left_rotation(inserted.parent)
                _right_rotation(inserted.parent)

            # Case 3 - right right
            elif not parent_left_of_grand and not inserted_left_of_parent:
                _flip_color(inserted.parent.parent)
                _flip_color(inserted.parent)
                _left_rotation(inserted.parent.parent)

            # Case 4 - right left
            elif not parent_left_of_grand and inserted_left_of_parent:
                _flip_color(inserted.parent.parent)
                _flip_color(inserted)
                _right_rotation(inserted.parent)
                _left_rotation(inserted.parent)

            # verify or update self.__root to be the greatest ancestor if it
            # is not already so, since we had to re-organize
            while self.__root.parent is not None:
                self.__root = self.__root.parent

    def delete(self, key):
        node = _find_node_by_key(self.__root, key)

        # if the node cannot be found, it cannot be deleted!
        if node is None:
            return KeyError()

        _delete_node(node)

    def get_content(self, key):
        found = _find_node_by_key(self.__root, key)
        if found is not None:
            return found.content
        raise KeyError()

    def _describe(self):
        def _describe_traversal(node):
            if node is None:
                return None
            return {
                'key': node.key,
                'color': node.color,
                'left': _describe_traversal(node.left),
                'right': _describe_traversal(node.right)
            }
        return _describe_traversal(self.__root)


if __name__ == '__main__':
    tree = RedBlackTree()
    tree.insert(100, 'a')
    tree.insert(200, 'b')
    tree.insert(300, 'c')
    tree.insert(500, 'e')
    tree.insert(700, 'f')
    tree.insert(800, 'g')
    tree.insert(900, 'h')
    import pprint
    pprint.pprint(tree._describe())
    tree.delete(500)
    pprint.pprint(tree._describe())
