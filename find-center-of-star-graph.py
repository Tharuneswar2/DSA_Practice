# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def findCenter(edges):
    # Create a dictionary to store the frequency of each node
    node_freq = {}
    
    # Iterate over each edge in the graph
    for edge in edges:
        # For each edge, increment the frequency of both nodes
        for node in edge:
            # If the node is already in the dictionary, increment its frequency
            if node in node_freq:
                node_freq[node] += 1
            # If the node is not in the dictionary, add it with a frequency of 1
            else:
                node_freq[node] = 1
                
    # The center of the star graph is the node with the highest frequency
    # Since it's a star graph, this node will be connected to all other nodes
    # So, its frequency will be equal to the number of edges
    # We can find this node by finding the node with the maximum frequency
    center = max(node_freq, key=node_freq.get)
    
    # Return the center of the star graph
    return center