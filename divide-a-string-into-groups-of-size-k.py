def divide_string(s, k, fill_value):
    # Initialize an empty list to store the result
    result = []
    
    # Initialize an empty string to store the current group
    current_group = ""
    
    # Iterate over the characters in the string
    for char in s:
        # Add the character to the current group
        current_group += char
        
        # If the length of the current group is equal to k
        if len(current_group) == k:
            # Add the current group to the result
            result.append(current_group)
            # Reset the current group
            current_group = ""
    
    # If there are remaining characters in the current group
    if current_group:
        # Fill the remaining characters with the fill value
        current_group += fill_value * (k - len(current_group))
        # Add the current group to the result
        result.append(current_group)
    
    # Return the result
    return result

def divide_string_alternative(s, k, fill_value):
    # Calculate the number of groups
    num_groups = len(s) // k + (1 if len(s) % k != 0 else 0)
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the range of the number of groups
    for i in range(num_groups):
        # Calculate the start index of the current group
        start = i * k
        # Calculate the end index of the current group
        end = (i + 1) * k
        # If the end index is greater than the length of the string
        if end > len(s):
            # Append the remaining characters in the string to the result
            result.append(s[start:] + fill_value * (k - (len(s) - start)))
        else:
            # Append the current group to the result
            result.append(s[start:end])
    
    # Return the result
    return result