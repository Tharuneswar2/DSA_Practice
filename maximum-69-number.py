# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maximum69Number (num):
    # Convert the number to a list of characters to easily manipulate digits
    num_list = list(str(num))
    
    # Iterate over each digit in the number
    for i in range(len(num_list)):
        # If the current digit is 6, replace it with 9 to maximize the number
        if num_list[i] == '6':
            num_list[i] = '9'
            # Break the loop as we only need to replace the first 6 with 9
            break
    
    # Join the list of characters back into a string and convert it to an integer
    return int(''.join(num_list))