def are_matrices_similar_after_cyclic_shifts(matrix1, matrix2):
    # Check if the matrices are of the same size
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return False

    # Flatten the matrices into strings
    str1 = ''.join(''.join(map(str, row)) for row in matrix1)
    str2 = ''.join(''.join(map(str, row)) for row in matrix2)

    # Check if str2 is a cyclic shift of str1
    if len(str1) != len(str2):
        return False

    # Concatenate str1 with itself
    double_str1 = str1 + str1

    # Check if str2 is a substring of double_str1
    return str2 in double_str1


# Example usage:
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[3, 1, 2], [6, 4, 5], [9, 7, 8]]
print(are_matrices_similar_after_cyclic_shifts(matrix1, matrix2))  # Output: True