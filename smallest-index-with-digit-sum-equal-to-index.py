def smallest_index_with_digit_sum_equal_to_index(n):
    # Iterate over all numbers from 1 to n
    for i in range(1, n + 1):
        # Convert the number to a string to calculate the sum of its digits
        digit_sum = sum(int(digit) for digit in str(i))
        
        # Check if the sum of the digits is equal to the number itself
        if digit_sum == i:
            # If it is, return the number
            return i

    # If no such number is found, return -1
    return -1

# Test the function
print(smallest_index_with_digit_sum_equal_to_index(100))