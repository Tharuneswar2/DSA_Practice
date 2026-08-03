# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def mirror_distance(n):
    # Convert the integer to a string to easily access each digit
    str_n = str(n)
    
    # Initialize variables to store the mirrored number and the maximum mirrored number
    mirrored_num = ''
    max_mirrored_num = ''
    
    # Iterate over each digit in the number
    for digit in str_n:
        # Calculate the mirrored digit by subtracting the digit from 9
        mirrored_digit = str(9 - int(digit))
        
        # Append the mirrored digit to the mirrored number
        mirrored_num += mirrored_digit
        
        # If the mirrored digit is greater than the original digit, update the maximum mirrored number
        if mirrored_digit > digit:
            max_mirrored_num = mirrored_num
            break
    
    # If no mirrored digit is greater than the original digit, the maximum mirrored number is the mirrored number itself
    if not max_mirrored_num:
        max_mirrored_num = mirrored_num
    
    # Calculate the distance between the original number and the maximum mirrored number
    distance = abs(int(max_mirrored_num) - n)
    
    return distance