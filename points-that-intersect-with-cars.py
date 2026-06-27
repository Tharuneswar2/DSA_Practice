def countPoints(points, queries):
    # Initialize an empty list to store the count of points that intersect with each query
    result = []
    
    # Iterate over each query
    for x, y, r in queries:
        # Initialize a counter for the current query
        count = 0
        
        # Iterate over each point
        for a, b in points:
            # Calculate the Euclidean distance between the point and the center of the query circle
            distance = (a - x) ** 2 + (b - y) ** 2
            
            # Check if the point lies within the query circle
            if distance <= r ** 2:
                # If the point intersects with the query circle, increment the counter
                count += 1
        
        # Append the count of points that intersect with the current query to the result list
        result.append(count)
    
    # Return the result list
    return result

# Example usage:
points = [[1, 3], [3, 3], [5, 3], [2, 2]]
queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
print(countPoints(points, queries))