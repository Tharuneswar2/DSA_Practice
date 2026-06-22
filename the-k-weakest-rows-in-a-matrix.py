def kWeakestRows(mat, k):
    # Create a list of tuples where each tuple contains the sum of each row and its index
    row_sums = [(sum(row), i) for i, row in enumerate(mat)]
    
    # Sort the list of tuples based on the sum of each row
    row_sums.sort()
    
    # Return the indices of the k weakest rows
    return [row[1] for row in row_sums[:k]]