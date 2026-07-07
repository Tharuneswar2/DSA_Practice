def maxEqualRowsAfterFlips(matrix):
    # Create a dictionary to store the frequency of each row pattern
    freq = {}
    
    # Iterate over each row in the matrix
    for row in matrix:
        # Convert the row into a tuple so it can be used as a dictionary key
        # If the first element of the row is 0, use the row as is; otherwise, flip the row
        key = tuple(x ^ row[0] for x in row)
        
        # Increment the frequency of the row pattern
        freq[key] = freq.get(key, 0) + 1
    
    # Return the maximum frequency found
    return max(freq.values())