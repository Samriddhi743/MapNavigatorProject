import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.nodes:
            self.nodes.add(from_node)
            self.edges[from_node] = {}
        if to_node not in self.nodes:
            self.nodes.add(to_node)
            self.edges[to_node] = {}
        self.edges[from_node][to_node] = weight

    def dijkstra(self, start, end):
        if start not in self.nodes or end not in self.nodes:
            return (float('inf'), [])  # If either start or end node is not in the graph

        # Priority queue for managing the minimum cost node
        queue = [(0, start)]
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        previous_nodes = {node: None for node in self.nodes}
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in self.edges.get(current_node, {}).items():
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))
        
        # Reconstruct the shortest path
        path = []
        node = end
        while node is not None:
            path.append(node)
            node = previous_nodes.get(node, None)
        
        path.reverse()
        
        if distances[end] == float('inf'):
            return (distances[end], [])  # No path found
        
        return (distances[end], path if path[0] == start else [])  # Ensure the path starts with the start node
