def reformatNumber(number: str) -> str:
    # Remove all non-digit characters from the string
    digits = ''.join(filter(str.isdigit, number))
    
    # Initialize an empty list to store the reformatted groups of digits
    groups = []
    
    # While there are still digits left to process
    while len(digits) > 0:
        # If there are 4 or more digits left, add a group of 3 digits
        if len(digits) >= 4:
            groups.append(digits[:3])
            digits = digits[3:]
        # If there are 2 digits left, add them as a group
        elif len(digits) == 2:
            groups.append(digits)
            digits = ''
        # If there is only 1 digit left, add it to the previous group
        elif len(digits) == 1:
            groups[-1] += digits
            digits = ''
    
    # Join the groups with '-' and return the result
    return '-'.join(groups)