# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def restoreFinishingOrder(numCourses, prerequisites):
    # Create an adjacency list to represent the graph
    graph = [[] for _ in range(numCourses)]
    
    # Create a list to store the in-degree of each node
    in_degree = [0] * numCourses
    
    # Populate the adjacency list and in-degree list
    for course, prereq in prerequisites:
        # Add an edge from the prerequisite to the course
        graph[prereq].append(course)
        # Increment the in-degree of the course
        in_degree[course] += 1
    
    # Create a queue to store nodes with in-degree 0
    queue = []
    for i in range(numCourses):
        # If a node has in-degree 0, add it to the queue
        if in_degree[i] == 0:
            queue.append(i)
    
    # Create a list to store the finishing order
    finishing_order = []
    
    # Perform topological sorting
    while queue:
        # Dequeue a node
        node = queue.pop(0)
        # Add the node to the finishing order
        finishing_order.append(node)
        
        # For each neighbor of the node
        for neighbor in graph[node]:
            # Decrement the in-degree of the neighbor
            in_degree[neighbor] -= 1
            # If the in-degree of the neighbor becomes 0, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If the length of the finishing order is not equal to the number of courses, there is a cycle
    if len(finishing_order) != numCourses:
        return []
    
    # Return the finishing order
    return finishing_order