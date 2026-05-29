def maximum69Number(num):
    # Convert the number to a list of characters for easier manipulation
    num_list = list(str(num))
    
    # Iterate over the list to find the first occurrence of '6'
    for i in range(len(num_list)):
        # If '6' is found, replace it with '9' to maximize the number
        if num_list[i] == '6':
            num_list[i] = '9'
            # Break the loop as we only need to replace the first '6'
            break
    
    # Join the list back into a string and convert it to an integer
    return int(''.join(num_list))