# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def validPath(n, edges, source, destination):
    # Create an adjacency list to represent the graph
    graph = [[] for _ in range(n)]
    
    # Populate the adjacency list with edges
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Assuming the graph is undirected
    
    # Use a set to keep track of visited nodes
    visited = set()
    
    # Define a helper function for DFS
    def dfs(node):
        # Mark the current node as visited
        visited.add(node)
        
        # If the current node is the destination, return True
        if node == destination:
            return True
        
        # Recur for all adjacent nodes that have not been visited yet
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        
        # If no path is found, return False
        return False
    
    # Start DFS from the source node
    return dfs(source)