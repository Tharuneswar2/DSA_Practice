# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def smallest_index_with_digit_sum_equal_to_index(n):
    # Iterate over the range from 1 to n (inclusive) to find the smallest index
    for i in range(1, n + 1):
        # Convert the index to a string to calculate the sum of its digits
        digit_sum = sum(int(digit) for digit in str(i))
        
        # Check if the sum of the digits is equal to the index
        if digit_sum == i:
            # If the condition is met, return the index
            return i
    
    # If no such index is found, return -1
    return -1