def balancedStringSplit(s):
    # Initialize a counter to keep track of the balance
    balance = 0
    
    # Initialize a counter to keep track of the number of balanced strings
    count = 0
    
    # Iterate over each character in the string
    for char in s:
        # If the character is 'L', decrement the balance
        if char == 'L':
            balance -= 1
        # If the character is 'R', increment the balance
        else:
            balance += 1
        
        # If the balance is zero, it means we have a balanced string
        if balance == 0:
            # Increment the count of balanced strings
            count += 1
    
    # Return the count of balanced strings
    return count