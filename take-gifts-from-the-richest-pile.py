# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maxEqualRowsAfterFlips(matrix):
    # Create a hashmap to store the frequency of each row pattern
    freq_map = {}
    
    # Iterate over each row in the matrix
    for row in matrix:
        # Check if the first element of the row is 0
        if row[0] == 0:
            # If it's 0, use the row as is
            pattern = tuple(row)
        else:
            # If it's 1, flip the row
            pattern = tuple(1 - x for x in row)
        
        # Increment the frequency of the pattern in the hashmap
        freq_map[pattern] = freq_map.get(pattern, 0) + 1
    
    # Return the maximum frequency found
    return max(freq_map.values())