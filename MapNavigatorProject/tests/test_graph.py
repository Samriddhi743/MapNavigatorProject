import unittest
from graph import Graph
# Implementing unittest for the testing purpose only.
class TestGraph(unittest.TestCase):
    # Setting up the initial graph values with the nodes.
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge('A', 'B', 1)
        self.graph.add_edge('A', 'C', 4)
        self.graph.add_edge('B', 'C', 2)
        self.graph.add_edge('C', 'D', 1)
        self.graph.add_edge('B', 'D', 5)

    def test_add_edge(self):
        self.graph.add_edge('D', 'E', 3)
        self.assertIn('D', self.graph.nodes)
        self.assertIn('E', self.graph.nodes)
        self.assertEqual(self.graph.edges['D']['E'], 3)

    def test_shortest_path(self):
        result = self.graph.dijkstra('A', 'D')
        self.assertEqual(result, (4, ['A', 'B', 'C', 'D']))

    def test_no_path(self):
        result = self.graph.dijkstra('A', 'Z')
        self.assertEqual(result, (float('inf'), []))

if __name__ == '__main__':
    unittest.main()
