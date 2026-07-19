# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def areMatricesSimilar(mat1, mat2):
    # First, we check if the two matrices are equal
    if mat1 == mat2:
        return True

    # If not, we perform cyclic shifts on the first matrix and check for equality
    # We only need to check for 3 cyclic shifts (up, down, left, right) because 
    # after 4 shifts, the matrix will be the same as the original
    for _ in range(3):
        # Perform a cyclic shift on the first matrix
        mat1 = shiftMatrix(mat1)
        
        # Check if the shifted matrix is equal to the second matrix
        if mat1 == mat2:
            return True

    # If none of the cyclic shifts result in equality, return False
    return False

def shiftMatrix(mat):
    # Perform a cyclic shift on the matrix by shifting each row to the right
    # and then shifting the last column to the first column
    n = len(mat)
    for i in range(n):
        # Shift each row to the right
        mat[i] = [mat[i][-1]] + mat[i][:-1]
    
    # Shift the last column to the first column
    last_col = [mat[i][-1] for i in range(n)]
    for i in range(n):
        mat[i] = [last_col[i]] + mat[i][:-1]
    
    return mat