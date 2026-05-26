def check_divisibility(n):
    # Convert the number into a string to easily access each digit
    str_n = str(n)
    
    # Initialize variables to store the sum and product of digits
    digit_sum = 0
    digit_product = 1
    
    # Iterate over each character (digit) in the string
    for digit in str_n:
        # Convert the character back into an integer
        int_digit = int(digit)
        
        # Add the digit to the sum
        digit_sum += int_digit
        
        # Multiply the digit with the product
        digit_product *= int_digit
    
    # Check if the number is divisible by both the sum and product of its digits
    if digit_sum != 0 and digit_product != 0 and n % digit_sum == 0 and n % digit_product == 0:
        return True
    else:
        return False

# Test the function
print(check_divisibility(123))  # Returns: False
print(check_divisibility(111))  # Returns: True