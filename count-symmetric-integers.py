def count_symmetric_integers(matrix):
    # Initialize count of symmetric integers
    count = 0
    
    # Iterate over the rows of the matrix
    for i in range(len(matrix)):
        # Iterate over the columns of the matrix
        for j in range(len(matrix[0])):
            # Check if the element is symmetric
            if matrix[i][j] == matrix[j][i]:
                # If the element is symmetric, increment the count
                count += 1
                
    # Return the count of symmetric integers
    return count

# Example usage:
matrix = [[1, 2, 3], [2, 1, 4], [3, 4, 5]]
print(count_symmetric_integers(matrix))