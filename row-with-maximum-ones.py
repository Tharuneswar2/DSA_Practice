# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def rowWithMax1s(arr, n, m):
    # Initialize max_row and max_count variables to store the row with maximum ones and the count of ones in that row
    max_row = -1
    max_count = 0
    
    # Iterate over each row in the 2D array
    for i in range(n):
        # Initialize low and high pointers for binary search
        low, high = 0, m - 1
        
        # Perform binary search to find the first occurrence of 1 in the current row
        while low <= high:
            mid = (low + high) // 2
            
            # If 1 is found, update the low pointer to mid + 1 to continue searching for the first occurrence of 1
            if arr[i][mid] == 1:
                high = mid - 1
            # If 0 is found, update the low pointer to mid + 1
            else:
                low = mid + 1
        
        # Calculate the count of ones in the current row
        count = m - low
        
        # Update max_row and max_count if the current row has more ones than the previous maximum
        if count > max_count:
            max_count = count
            max_row = i
    
    # Return the row with maximum ones
    return max_row