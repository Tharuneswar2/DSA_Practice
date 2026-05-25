def is_rotation(matrix1, matrix2):
    # Check if the matrices are the same size
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return False

    # Check if matrix2 is a rotation of matrix1
    def is_equal(matrix1, matrix2):
        return all(all(a == b for a, b in zip(row1, row2)) for row1, row2 in zip(matrix1, matrix2))

    # Check all four possible rotations
    if is_equal(matrix1, matrix2):
        return True
    if is_equal(matrix1, [list(reversed(x)) for x in zip(*matrix2)]):
        return True
    if is_equal(matrix1, [list(reversed(x)) for x in reversed(matrix2)]):
        return True
    if is_equal(matrix1, [list(x) for x in reversed(list(zip(*matrix2)))]):
        return True

    # If none of the rotations match, return False
    return False

def is_rotation_transpose(matrix1, matrix2):
    # Check if the matrices are the same size
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return False

    # Check if matrix2 is a rotation of matrix1
    def rotate(matrix):
        return [list(reversed(x)) for x in zip(*matrix)]

    # Check all four possible rotations
    for _ in range(4):
        if matrix1 == matrix2:
            return True
        matrix2 = rotate(matrix2)

    # If none of the rotations match, return False
    return False