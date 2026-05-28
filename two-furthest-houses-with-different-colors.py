def maxDistance(colors):
    # Initialize two pointers, one at the start and one at the end of the list
    left, right = 0, len(colors) - 1
    
    # If the colors at the start and end are different, return the distance
    if colors[left] != colors[right]:
        return right - left
    
    # If the colors at the start and end are the same, move the pointers towards each other
    while left < right:
        # Move the left pointer to the right until we find a different color
        if colors[left] != colors[right]:
            break
        left += 1
        
        # Move the right pointer to the left until we find a different color
        if colors[left] != colors[right]:
            break
        right -= 1
    
    # Return the maximum distance
    return max(right - left, len(colors) - 1 - left, right)