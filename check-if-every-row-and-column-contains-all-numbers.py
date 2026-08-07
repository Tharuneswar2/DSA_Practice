# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def checkValid(matrix):
    n = len(matrix)  # Get the size of the matrix
    for i in range(n):  # Iterate over each row
        row = set()  # Initialize a set to store unique elements in the row
        col = set()  # Initialize a set to store unique elements in the column
        for j in range(n):  # Iterate over each column
            row.add(matrix[i][j])  # Add the element to the row set
            col.add(matrix[j][i])  # Add the element to the column set
        if len(row) != n or len(col) != n:  # If the length of the set is not equal to n, return False
            return False
    return True  # If all rows and columns contain all numbers, return True