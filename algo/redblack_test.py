import unittest
import redblack


def _create_tree():
    root = redblack.RedBlackNode(500, 'e', redblack.BLACK)

    redblack._insert_at_node(root, 200, 'b', redblack.RED)
    redblack._insert_at_node(root.left, 100, 'a', redblack.BLACK)
    redblack._insert_at_node(root.left, 300, 'c', redblack.BLACK)

    redblack._insert_at_node(root, 800, 'g', redblack.RED)
    redblack._insert_at_node(root.right, 700, 'f', redblack.BLACK)
    redblack._insert_at_node(root.right, 900, 'h', redblack.BLACK)

    return root


def _insert_tree():
    tree = redblack.RedBlackTree()
    tree.insert(100, 'a')
    tree.insert(200, 'b')
    tree.insert(300, 'c')
    tree.insert(500, 'e')
    tree.insert(700, 'f')
    tree.insert(800, 'g')
    tree.insert(900, 'h')

    return tree


class TestRedBlack(unittest.TestCase):
    def test_find_closest_ancestor_by_key(self):
        tree = _create_tree()
        found = redblack._find_closest_ancestor_by_key(tree, 750)
        self.assertEqual(found.key, 700)

    def test_find_sibling(self):
        tree = _create_tree()
        self.assertEqual(redblack._find_sibling(tree.left.right).key, 100)
        self.assertEqual(redblack._find_sibling(tree), None)

    def test_get_node_color(self):
        tree = _create_tree()
        self.assertEqual(redblack._get_node_color(tree.left.right),
                         redblack.BLACK)

    def test_flip_color(self):
        node = redblack.RedBlackNode(1)
        redblack._flip_color(node)
        self.assertEqual(node.color, redblack.BLACK)

    def test_left_rotation(self):
        tree = _create_tree()
        redblack._left_rotation(tree.left)
        self.assertEqual(tree.left.left.left.key, 100)  # rotated

        tree = _create_tree()
        redblack._left_rotation(tree)
        self.assertEqual(tree.parent.parent, None)  # rotated, top of the tree
        self.assertEqual(tree.parent.key, 800)
        self.assertEqual(tree.left.key, 200)

        tree = _create_tree()
        self.assertRaises(redblack.NullNodeError,
                          redblack._left_rotation,
                          tree.left.right)  # not possible

    def test_right_rotation(self):
        tree = _create_tree()
        redblack._right_rotation(tree.left)
        self.assertEqual(tree.left.right.right.key, 300)  # rotated

        tree = _create_tree()
        redblack._right_rotation(tree)
        self.assertEqual(tree.parent.parent, None)  # rotated, top of the tree
        self.assertEqual(tree.parent.key, 200)
        self.assertEqual(tree.left.key, 300)

        tree = _create_tree()
        self.assertRaises(redblack.NullNodeError,
                          redblack._right_rotation,
                          tree.right.left)  # not possible

    def test_find_node_by_key(self):
        tree = _create_tree()
        self.assertEqual(redblack._find_node_by_key(tree, 700).key,
                         700)  # findable
        self.assertRaises(KeyError,
                          redblack._find_node_by_key,
                          tree,
                          750)  # not findable
        self.assertRaises(KeyError,
                          redblack._find_node_by_key,
                          None,
                          700)  # no tree provided

    def test_red_uncle_recolor(self):
        tree = _create_tree()
        redblack._red_uncle_recolor(tree.left)
        self.assertEqual(tree.color, redblack.RED)
        self.assertEqual(tree.left.color, redblack.BLACK)
        self.assertEqual(tree.right.color, redblack.BLACK)

    def test_describe(self):
        tree = _insert_tree()
        result = tree._describe()
        self.assertEqual(result['right']['left']['key'], 300)

    def test_insert_and_get(self):
        tree = _insert_tree()
        self.assertEqual(tree.get_content(800), 'g')
        self.assertRaises(KeyError,
                          tree.get_content,
                          600)


if __name__ == '__main__':
    unittest.main()
