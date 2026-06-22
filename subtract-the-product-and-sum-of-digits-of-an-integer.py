def subtractProductAndSum(n: int) -> int:
    # Convert the integer into a string to easily access each digit
    str_n = str(n)
    
    # Initialize variables to store the product and sum of digits
    product_of_digits = 1
    sum_of_digits = 0
    
    # Iterate over each character (digit) in the string
    for digit in str_n:
        # Convert the character back into an integer
        int_digit = int(digit)
        
        # Multiply the current product by the current digit
        product_of_digits *= int_digit
        
        # Add the current digit to the sum
        sum_of_digits += int_digit
    
    # Return the difference between the product and sum of digits
    return product_of_digits - sum_of_digits