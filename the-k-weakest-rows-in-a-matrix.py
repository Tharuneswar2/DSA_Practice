# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def kWeakestRows(mat, k):
    # Create a list of tuples where each tuple contains the sum of each row and its index
    # The sum of each row represents the number of soldiers in that row
    rows = [(sum(row), i) for i, row in enumerate(mat)]
    
    # Sort the list of tuples based on the sum of each row and its index
    # If two rows have the same number of soldiers, the row with the smaller index comes first
    rows.sort()
    
    # Return the indices of the k weakest rows
    # We use a list comprehension to extract the indices from the sorted list of tuples
    return [row[1] for row in rows[:k]]