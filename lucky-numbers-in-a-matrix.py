# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def luckyNumbers(matrix):
    # First, we transpose the matrix to easily find the minimum in each row
    transposed_matrix = list(map(list, zip(*matrix)))
    
    # Initialize an empty set to store the lucky numbers
    lucky_nums = set()
    
    # Iterate over each row in the original matrix
    for row in matrix:
        # Find the minimum in the current row
        min_in_row = min(row)
        
        # Find the column index of the minimum in the current row
        col_idx = row.index(min_in_row)
        
        # Check if the minimum in the current row is the maximum in its column
        if min_in_row == max(transposed_matrix[col_idx]):
            # If it is, add it to the set of lucky numbers
            lucky_nums.add(min_in_row)
    
    # Return the list of lucky numbers
    return list(lucky_nums)