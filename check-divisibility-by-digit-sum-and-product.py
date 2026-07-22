# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def check_divisibility(n):
    # Convert the number into a string to easily access each digit
    str_n = str(n)
    
    # Initialize variables to store the sum and product of digits
    sum_of_digits = 0
    product_of_digits = 1
    
    # Iterate over each character (digit) in the string
    for digit in str_n:
        # Convert the character back into an integer
        int_digit = int(digit)
        
        # Add the digit to the sum
        sum_of_digits += int_digit
        
        # Multiply the digit with the product
        product_of_digits *= int_digit
    
    # Check if the number is divisible by both the sum and product of its digits
    if sum_of_digits != 0 and product_of_digits != 0 and n % sum_of_digits == 0 and n % product_of_digits == 0:
        return True
    else:
        return False