def thousandSeparator(n):
    # Convert the number to a string to easily manipulate its digits
    str_n = str(n)
    
    # Initialize an empty string to store the result
    result = ""
    
    # Initialize a counter to keep track of the number of digits processed
    count = 0
    
    # Iterate over the digits of the number in reverse order
    for i in range(len(str_n) - 1, -1, -1):
        # Add the current digit to the result
        result = str_n[i] + result
        
        # Increment the counter
        count += 1
        
        # If the counter is a multiple of 3 and not equal to the length of the number, add a dot to the result
        if count % 3 == 0 and count != len(str_n):
            result = "." + result
    
    # Return the result
    return result