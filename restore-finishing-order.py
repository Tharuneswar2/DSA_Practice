from collections import defaultdict, deque

def restoreFinishingOrder(numCourses, prerequisites):
    # Create a graph and in-degree dictionary
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(numCourses)}
    
    # Populate the graph and in-degree dictionary
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Initialize a queue with courses that have no prerequisites
    queue = deque([course for course in in_degree if in_degree[course] == 0])
    
    # Initialize the result list
    result = []
    
    # Perform topological sorting
    while queue:
        course = queue.popleft()
        result.append(course)
        
        # Decrease the in-degree of neighboring courses
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If there's a cycle, return an empty list
    if len(result) != numCourses:
        return []
    
    # Return the result in reverse order (finishing order)
    return result[::-1]