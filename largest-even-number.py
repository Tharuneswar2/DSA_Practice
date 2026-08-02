# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def largest_even_number(num_str):
    # Convert the input string into a list of characters for easier manipulation
    num_list = list(num_str)
    
    # Initialize variables to store the maximum even digit and its index
    max_even_digit = -1
    max_even_digit_index = -1
    
    # Iterate over the list of digits from right to left
    for i in range(len(num_list) - 1, -1, -1):
        # Check if the current digit is even
        if int(num_list[i]) % 2 == 0:
            # If the current even digit is greater than the max even digit found so far, update max even digit and its index
            if int(num_list[i]) > max_even_digit:
                max_even_digit = int(num_list[i])
                max_even_digit_index = i
                
    # If no even digit is found, return an empty string
    if max_even_digit == -1:
        return ""
    
    # Swap the max even digit with the last digit
    num_list[len(num_list) - 1], num_list[max_even_digit_index] = num_list[max_even_digit_index], num_list[len(num_list) - 1]
    
    # Join the list of digits back into a string and return the result
    return "".join(num_list)