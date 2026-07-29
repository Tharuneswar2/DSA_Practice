# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def findDiagonalOrder(nums):
    # Initialize a hashmap to store the diagonal elements
    diagonal = {}
    
    # Iterate over each row in the grid
    for i in range(len(nums)):
        # Iterate over each element in the current row
        for j in range(len(nums[i])):
            # Calculate the diagonal index (i + j)
            diagonal_idx = i + j
            
            # If the diagonal index is not in the hashmap, add it
            if diagonal_idx not in diagonal:
                diagonal[diagonal_idx] = []
            
            # Append the current element to the corresponding diagonal in the hashmap
            diagonal[diagonal_idx].append(nums[i][j])
    
    # Initialize the result list
    result = []
    
    # Iterate over the diagonals in the hashmap
    for diagonal_idx in diagonal:
        # If the diagonal index is even, append the elements in reverse order
        if diagonal_idx % 2 == 0:
            result.extend(reversed(diagonal[diagonal_idx]))
        # If the diagonal index is odd, append the elements in normal order
        else:
            result.extend(diagonal[diagonal_idx])
    
    # Return the result list
    return result