class Vertex:
    def __init__(self, content=None, edges=None):
        self.content = content
        if edges is None:
            self.edges = []
        else:
            self.edges = edges


class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, x, y):
        self.graph[x].edges.append(y)

    def add(self, content=None, edges=None):
        self.graph.append(Vertex(content, edges))

    def print(self):
        for head in range(len(self.graph)):
            print(self.graph[head].content, '=', head, end=' ')
            for v in self.graph[head].edges:
                print('->', v, end=' ')
            print()

    def bfs(self, needle, head=0, trace=False):
        # track seen vertices to prevent looping
        seen = [False] * len(self.graph)

        # keep track of additional found nodes needing processing
        # and seed the queue with our root node
        queue = [head]
        seen[head] = True

        # keep processing until queue is empty
        while queue:

            # define a new search root
            head = queue.pop(0)
            if trace:
                print(head, end=' ')

            # if the needle is found in this vertex, return it
            if self.graph[head].content == needle:
                if trace:
                    print('found')
                return head

            # queue unseen peers for searching
            for neighbor in self.graph[head].edges:
                if not seen[neighbor]:
                    seen[neighbor] = True
                    queue.append(neighbor)

        # if the needle is not found, return None
        if trace:
            print('not found')
        return None

    def dfs(self, needle, head=0, trace=False, seen=None):
        # track seen vertices to prevent looping
        seen = [False] * len(self.graph)

        def _dfs(self, needle, head, trace, seen):
            if trace:
                print(head, end=' ')

            # if this vertex contains the needle, return this vertex index
            # seen is now irrelevant, but we return it anyway (we could return None instead)
            if self.graph[head].content == needle:
                if trace:
                    print('found')
                return head, seen

            # for each neighbor, recurse into it to search
            for neighbor in self.graph[head].edges:
                result = None

                # only recurse into a neighbor if it has not been seen before
                if not seen[neighbor]:
                    seen[neighbor] = True
                    result, seen = _dfs(self, needle, neighbor, trace, seen)

                # if the result is ever a value other than None, we have success
                # seen is now irrelevant, but we return it anyway (we could return None instead)
                if result is not None:
                    return result, seen

            # if we reached this point, this subtree does not contain the needle
            # return None and the updated seen list
            return None, seen

        result, _ = _dfs(self, needle, head, trace, seen)
        if trace and result is None:
            print('not found')
        return result


if __name__ == "__main__":
    g = Graph()
    g.add('a', [1, 2, 5])
    g.add('b', [0])
    g.add('c', [4])
    g.add('d', [1, 2])
    g.add('e', [4])
    g.add('f', [0])
    g.print()
