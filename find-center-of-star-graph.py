# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def findCenter(edges):
    # Create a dictionary to store the frequency of each node
    freq = {}
    
    # Iterate over each edge in the graph
    for edge in edges:
        # For each edge, increment the frequency of both nodes
        for node in edge:
            # If the node is already in the dictionary, increment its frequency
            if node in freq:
                freq[node] += 1
            # If the node is not in the dictionary, add it with a frequency of 1
            else:
                freq[node] = 1
                
    # The center of the star graph is the node with the highest frequency
    # Since it's a star graph, there can only be one node with the highest frequency
    # So, we return the node with the highest frequency
    return max(freq, key=freq.get)