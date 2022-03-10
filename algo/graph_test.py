import unittest
import graph


def _create_graph():
    g = graph.Graph()
    g.add('a', [1, 2, 5])
    g.add('b', [0])
    g.add('c', [4])
    g.add('d', [1, 2])
    g.add('e', [4])
    g.add('f', [0])
    return g


class TestGraph(unittest.TestCase):

    def test_graph_bfs(self):
        g = _create_graph()
        self.assertEqual(g.bfs('e', 0), 4)
        self.assertEqual(g.bfs('d', 0), None)
        self.assertEqual(g.bfs('e', 3), 4)
        self.assertEqual(g.bfs('d', 3), 3)

    def test_graph_dfs(self):
        g = _create_graph()
        self.assertEqual(g.dfs('e', 0), 4)
        self.assertEqual(g.dfs('d', 0), None)
        self.assertEqual(g.dfs('e', 3), 4)
        self.assertEqual(g.dfs('d', 3), 3)


if __name__ == '__main__':
    unittest.main()
