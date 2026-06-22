def find_vertex_degrees(graph):
    # Initialize a dictionary to store the degree of each vertex
    vertex_degrees = {}

    # Iterate over each vertex in the graph
    for vertex in graph:
        # Initialize the degree of the current vertex to 0
        vertex_degrees[vertex] = 0

        # Iterate over each neighbor of the current vertex
        for neighbor in graph[vertex]:
            # Increment the degree of the current vertex by 1
            vertex_degrees[vertex] += 1

    # Return the dictionary containing the degree of each vertex
    return vertex_degrees


# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

vertex_degrees = find_vertex_degrees(graph)
for vertex, degree in vertex_degrees.items():
    print(f"The degree of vertex {vertex} is {degree}")