# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countMonotoneNumbers(n):
    # Initialize a variable to store the count of monotone numbers
    count = 0
    
    # Iterate over all numbers from 1 to n
    for i in range(1, n+1):
        # Convert the number to a string to easily access each digit
        str_i = str(i)
        
        # Initialize variables to track if the number is increasing or decreasing
        is_increasing = True
        is_decreasing = True
        
        # Iterate over each digit in the number
        for j in range(1, len(str_i)):
            # If the current digit is less than the previous digit, the number is not increasing
            if str_i[j] < str_i[j-1]:
                is_increasing = False
            # If the current digit is greater than the previous digit, the number is not decreasing
            if str_i[j] > str_i[j-1]:
                is_decreasing = False
        
        # If the number is either increasing or decreasing, increment the count
        if is_increasing or is_decreasing:
            count += 1
    
    # Return the count of monotone numbers
    return count