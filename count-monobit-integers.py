def countMonotoneNumbers(n):
    # Initialize a dictionary to store the count of monotone numbers for each digit
    dp = {i: 1 for i in range(10)}

    # Iterate over the number of digits from 2 to n
    for digits in range(2, n + 1):
        # Initialize a dictionary to store the count of monotone numbers for the current number of digits
        new_dp = {i: 0 for i in range(10)}
        
        # Iterate over the possible last digits
        for last_digit in range(10):
            # Iterate over the possible second last digits
            for second_last_digit in range(last_digit + 1):
                # Update the count of monotone numbers for the current last digit
                new_dp[last_digit] += dp[second_last_digit]
        
        # Update the dictionary for the next iteration
        dp = new_dp

    # Calculate the total count of monotone numbers
    total_count = sum(dp.values())

    # Return the total count
    return total_count