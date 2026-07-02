def maxContainersOnShip(heights):
    # Initialize two pointers, one at the start and one at the end of the list
    left = 0
    right = len(heights) - 1
    
    # Initialize the maximum area
    max_area = 0
    
    # Continue the loop until the two pointers meet
    while left < right:
        # Calculate the width of the current area
        width = right - left
        
        # Calculate the height of the current area, which is the minimum of the two lines
        height = min(heights[left], heights[right])
        
        # Calculate the current area
        area = width * height
        
        # Update the maximum area if the current area is larger
        max_area = max(max_area, area)
        
        # Move the pointer of the shorter line towards the other pointer
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    # Return the maximum area
    return max_area

# Test the function
heights = [1,8,6,2,5,4,8,3,7]
print(maxContainersOnShip(heights))  # Output: 49