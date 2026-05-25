def findDigits(n):
    # Convert the number to a string to easily access each digit
    str_n = str(n)
    
    # Initialize a counter to store the count of digits that divide the number
    count = 0
    
    # Iterate over each digit in the string
    for digit in str_n:
        # Convert the digit back to an integer
        int_digit = int(digit)
        
        # Check if the digit is non-zero and the number is divisible by the digit
        if int_digit != 0 and n % int_digit == 0:
            # If the condition is met, increment the counter
            count += 1
    
    # Return the count of digits that divide the number
    return count