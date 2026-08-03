# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def findRotation(matrix, target):
    # First, we check if the target matrix is the same as the original matrix
    if matrix == target:
        return True
    
    # We define the number of rows and columns in the matrix
    n = len(matrix)
    
    # We perform three rotations and check if the target matrix matches the rotated matrix
    for _ in range(3):
        # We transpose the matrix (swap rows with columns)
        matrix = list(zip(*matrix))
        
        # We reverse each row in the transposed matrix
        matrix = [list(reversed(row)) for row in matrix]
        
        # We check if the rotated matrix matches the target matrix
        if matrix == target:
            return True
    
    # If none of the rotations match the target matrix, we return False
    return False