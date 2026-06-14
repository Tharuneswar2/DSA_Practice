def findCenter(edges):
    # Create a dictionary to store the frequency of each node
    node_freq = {}
    
    # Iterate over each edge in the graph
    for edge in edges:
        # For each edge, increment the frequency of both nodes
        for node in edge:
            if node in node_freq:
                node_freq[node] += 1
            else:
                node_freq[node] = 1
    
    # The center of the star graph is the node with the highest frequency
    # Since it's a star graph, this node will be connected to all other nodes
    # So, its frequency will be equal to the number of edges
    center = [node for node, freq in node_freq.items() if freq == len(edges)]
    
    # Return the center of the star graph
    return center[0]