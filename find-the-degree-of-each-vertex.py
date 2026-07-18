# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def find_vertex_degrees(graph):
    # Initialize an empty dictionary to store the degree of each vertex
    vertex_degrees = {}

    # Iterate over each vertex in the graph
    for vertex in graph:
        # Initialize the degree of the current vertex to 0
        vertex_degrees[vertex] = 0

        # Iterate over each neighbor of the current vertex
        for neighbor in graph[vertex]:
            # Increment the degree of the current vertex by 1
            vertex_degrees[vertex] += 1

            # If the neighbor is not the same as the current vertex (to avoid counting self-loops twice)
            if neighbor != vertex:
                # If the neighbor is not already in the dictionary, add it with a degree of 1
                if neighbor not in vertex_degrees:
                    vertex_degrees[neighbor] = 1
                # If the neighbor is already in the dictionary, increment its degree by 1
                else:
                    vertex_degrees[neighbor] += 1

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

print(find_vertex_degrees(graph))