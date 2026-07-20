# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maxDistance(self, color: list[int]) -> int:
    # Initialize variables to store the maximum distance and the indices of the furthest houses with different colors
    max_dist = 0
    left, right = 0, len(color) - 1
    
    # Traverse the list from the left and find the first house with a different color
    while color[left] == color[0]:
        left += 1
    
    # Traverse the list from the right and find the first house with a different color
    while color[right] == color[-1]:
        right -= 1
    
    # Update the maximum distance
    max_dist = max(max_dist, right - left)
    
    # Traverse the list from the left and find the furthest house with a different color
    for i in range(len(color)):
        # If the current house has a different color than the first house
        if color[i] != color[0]:
            # Update the maximum distance
            max_dist = max(max_dist, i - left)
        # If the current house has a different color than the last house
        if color[i] != color[-1]:
            # Update the maximum distance
            max_dist = max(max_dist, right - i)
    
    # Return the maximum distance
    return max_dist