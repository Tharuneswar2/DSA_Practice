# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def reformatNumber(number):
    # Remove all non-digit characters from the phone number
    digits = ''.join(filter(str.isdigit, number))
    
    # Initialize an empty list to store the reformatted phone number
    reformatted_number = []
    
    # Loop through the digits until there are 4 or less digits left
    while len(digits) > 4:
        # If there are more than 4 digits left, append the first 3 digits to the reformatted number
        if len(digits) > 4:
            reformatted_number.append(digits[:3])
            # Remove the first 3 digits from the remaining digits
            digits = digits[3:]
        # If there are exactly 4 digits left, append the first 2 digits and the last 2 digits separately to the reformatted number
        else:
            reformatted_number.append(digits[:2])
            reformatted_number.append(digits[2:])
            # Break the loop since there are no more digits left
            break
    
    # If there are 2 or less digits left, append them to the reformatted number
    if digits:
        reformatted_number.append(digits)
    
    # Join the reformatted number with '-' and return the result
    return '-'.join(reformatted_number)