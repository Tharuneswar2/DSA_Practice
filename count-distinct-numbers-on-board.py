# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def distinctNumbers(n, k):
    # Initialize a set to store unique numbers
    unique_nums = set()
    
    # Iterate over each row in the board
    for i in range(1, n+1):
        # Iterate over each column in the board
        for j in range(1, n+1):
            # Calculate the number at the current position
            num = (i-1) * n + j
            
            # Check if the number is divisible by k
            if num % k == 0:
                # Add the number to the set
                unique_nums.add(num)
    
    # Return the count of unique numbers
    return len(unique_nums)