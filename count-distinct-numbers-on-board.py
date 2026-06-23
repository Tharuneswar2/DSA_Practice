def distinct_numbers_on_board(n):
    # Initialize a set to store unique numbers
    unique_numbers = set()
    
    # Iterate over each row of the board
    for i in range(1, n + 1):
        # Iterate over each column of the board
        for j in range(1, n + 1):
            # Calculate the number at the current position
            num = (i - 1) * n + j
            
            # Add the number to the set
            unique_numbers.add(num)
    
    # Return the count of unique numbers
    return len(unique_numbers)

# Test the function
print(distinct_numbers_on_board(5))