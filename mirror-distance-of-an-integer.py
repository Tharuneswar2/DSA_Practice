def mirror_distance(n):
    # Convert the integer to a string to easily access each digit
    str_n = str(n)
    
    # Initialize the minimum distance
    min_distance = float('inf')
    
    # Iterate over each possible mirror number
    for i in range(10**len(str_n)):
        # Convert the current number to a string
        str_i = str(i).zfill(len(str_n))
        
        # Check if the current number is a mirror of the input number
        if str_i == str_n[::-1]:
            # Calculate the distance between the current number and the input number
            distance = abs(n - i)
            
            # Update the minimum distance if the current distance is smaller
            min_distance = min(min_distance, distance)
    
    # Return the minimum distance
    return min_distance

def mirror_distance_optimized(n):
    # Convert the integer to a string to easily access each digit
    str_n = str(n)
    
    # Initialize the minimum distance
    min_distance = float('inf')
    
    # Iterate over each possible mirror number with the same number of digits
    for i in range(10**(len(str_n)-1), 10**len(str_n)):
        # Convert the current number to a string
        str_i = str(i)
        
        # Check if the current number is a mirror of the input number
        if str_i == str_n[::-1]:
            # Calculate the distance between the current number and the input number
            distance = abs(n - i)
            
            # Update the minimum distance if the current distance is smaller
            min_distance = min(min_distance, distance)
    
    # If no mirror number is found, try numbers with one less digit
    if min_distance == float('inf'):
        return mirror_distance_optimized(int(str_n[:-1]))
    
    # Return the minimum distance
    return min_distance