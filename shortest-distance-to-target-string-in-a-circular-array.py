def shortestDistance(words, target, start):
    n = len(words)
    idx = [i for i, word in enumerate(words) if word == target]
    if not idx: return -1
    
    # Calculate the distance from the start index to the target string
    dist = [abs(i - start) for i in idx]
    
    # Consider the circular nature of the array
    circular_dist = [min(i + 1, n - i) for i in idx]
    
    # Combine the distances and return the minimum
    return min(min(dist), min(circular_dist))

def shortestDistanceOptimized(words, target, start):
    n = len(words)
    idx = [i for i, word in enumerate(words) if word == target]
    if not idx: return -1
    
    # Initialize the minimum distance
    min_dist = float('inf')
    
    # Iterate over the indices of the target string
    for i in idx:
        # Calculate the distance from the start index to the target string
        dist = abs(i - start)
        
        # Consider the circular nature of the array
        circular_dist = min(i + 1, n - i)
        
        # Update the minimum distance
        min_dist = min(min_dist, dist, circular_dist)
    
    return min_dist