def check_valid(matrix):
    n = len(matrix)
    
    # Check rows
    for row in matrix:
        # Create a set of numbers from 1 to n
        nums = set(range(1, n + 1))
        
        # Remove numbers present in the row from the set
        for num in row:
            if num in nums:
                nums.remove(num)
        
        # If the set is not empty, it means some numbers are missing in the row
        if nums:
            return False
    
    # Check columns
    for col in range(n):
        # Create a set of numbers from 1 to n
        nums = set(range(1, n + 1))
        
        # Remove numbers present in the column from the set
        for row in matrix:
            if row[col] in nums:
                nums.remove(row[col])
        
        # If the set is not empty, it means some numbers are missing in the column
        if nums:
            return False
    
    # If no missing numbers are found in rows and columns, return True
    return True

# Example usage:
matrix = [
    [1, 2, 3],
    [3, 1, 2],
    [2, 3, 1]
]
print(check_valid(matrix))  # Output: True