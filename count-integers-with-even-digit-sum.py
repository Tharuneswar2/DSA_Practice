# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def countEven(num):
    # Initialize count variable to store the count of integers with even digit sum
    count = 0
    
    # Iterate over the range from 1 to num (inclusive)
    for i in range(1, num + 1):
        # Convert the integer to a string to easily extract its digits
        str_i = str(i)
        
        # Initialize sum variable to store the sum of digits
        sum_of_digits = 0
        
        # Iterate over each character (digit) in the string
        for digit in str_i:
            # Add the integer value of the digit to the sum
            sum_of_digits += int(digit)
        
        # Check if the sum of digits is even
        if sum_of_digits % 2 == 0:
            # If the sum is even, increment the count
            count += 1
    
    # Return the count of integers with even digit sum
    return count