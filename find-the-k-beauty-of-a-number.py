def divisorSubstrings(n: int, k: int) -> int:
    # Convert the number to a string to easily extract substrings
    str_n = str(n)
    
    # Initialize a counter for the k-beauty
    beauty = 0
    
    # Iterate over the string representation of the number
    for i in range(len(str_n)):
        # Extract a substring of length k
        substring = str_n[i:i+k]
        
        # Check if the substring is a divisor of the number
        if int(substring) != 0 and n % int(substring) == 0:
            # If it is, increment the beauty counter
            beauty += 1
    
    # Return the k-beauty of the number
    return beauty