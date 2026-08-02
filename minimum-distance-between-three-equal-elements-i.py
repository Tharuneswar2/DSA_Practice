# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minDistance(arr):
    # Initialize minimum distance as infinity
    min_dist = float('inf')
    
    # Iterate over the array with three nested loops to consider all possible triplets
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                # Check if the current triplet has equal elements
                if arr[i] == arr[j] == arr[k]:
                    # Calculate the distance between the first and last elements of the triplet
                    dist = k - i
                    # Update the minimum distance if the current distance is smaller
                    min_dist = min(min_dist, dist)
    
    # If no triplet with equal elements is found, return -1
    if min_dist == float('inf'):
        return -1
    else:
        return min_dist