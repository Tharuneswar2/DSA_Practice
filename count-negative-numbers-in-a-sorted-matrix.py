def countNegatives(grid):
    # Initialize count of negative numbers
    count = 0
    
    # Iterate over each row in the grid
    for row in grid:
        # Use binary search to find the first negative number in the row
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            # If the middle element is negative, update the right pointer
            if row[mid] < 0:
                right = mid - 1
            # If the middle element is non-negative, update the left pointer
            else:
                left = mid + 1
        
        # The number of negative numbers in the row is the difference between the length of the row and the left pointer
        count += len(row) - left
    
    # Return the total count of negative numbers
    return count