# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countNegatives(grid):
    # Initialize count of negative numbers to 0
    count = 0
    
    # Iterate over each row in the grid
    for row in grid:
        # Use binary search to find the first negative number in the row
        # Initialize two pointers, one at the start and one at the end of the row
        left, right = 0, len(row) - 1
        
        # Continue the binary search until the two pointers meet
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # If the middle element is negative, update the right pointer
            if row[mid] < 0:
                # If the middle element is the first element or the element before it is not negative, 
                # we have found the first negative number, so update the count and break the loop
                if mid == 0 or row[mid - 1] >= 0:
                    count += len(row) - mid
                    break
                # Otherwise, update the right pointer
                right = mid - 1
            # If the middle element is not negative, update the left pointer
            else:
                left = mid + 1
                
    # Return the total count of negative numbers
    return count