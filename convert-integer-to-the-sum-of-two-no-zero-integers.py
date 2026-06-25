def getNoZeroIntegers(n: int):
    # Start from 1 and go up to n-1
    for i in range(1, n):
        # Convert the numbers to strings to check if they contain zeros
        str_i = str(i)
        str_n_minus_i = str(n - i)
        
        # Check if both numbers do not contain zeros
        if '0' not in str_i and '0' not in str_n_minus_i:
            # If both numbers do not contain zeros, return them
            return [i, n - i]