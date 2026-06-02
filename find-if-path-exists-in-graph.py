from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_valid(self, v, visited, path):
        # Check if the current vertex is already in the path
        if v in path:
            return False
        # Mark the current vertex as visited
        visited[v] = True
        # Add the current vertex to the path
        path.append(v)
        # If the current vertex is the destination, return True
        if v == self.V - 1:
            return True
        # Recur for all the adjacent vertices of the current vertex
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_valid(neighbor, visited, path):
                    return True
        # If no path is found, remove the current vertex from the path and return False
        path.pop()
        return False

    def is_path_exists(self, source, destination):
        # Create a visited array and initialize all entries as False
        visited = [False] * self.V
        # Create a path array to store the path
        path = []
        # Check if a path exists from the source to the destination
        return self.is_valid(source, visited, path)


# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
print(g.is_path_exists(0, 4))  # Output: True
print(g.is_path_exists(0, 3))  # Output: True
print(g.is_path_exists(1, 4))  # Output: False