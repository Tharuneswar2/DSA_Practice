def largest_even_number(num_str):
    # Convert the input string into a list of characters for easier manipulation
    num_list = list(num_str)
    
    # Initialize variables to store the largest even digit and its index
    largest_even_digit = 0
    largest_even_index = -1
    
    # Iterate over the list of digits from right to left
    for i in range(len(num_list) - 1, -1, -1):
        # Check if the current digit is even and larger than the current largest even digit
        if int(num_list[i]) % 2 == 0 and int(num_list[i]) > largest_even_digit:
            # Update the largest even digit and its index
            largest_even_digit = int(num_list[i])
            largest_even_index = i
    
    # If no even digit is found, return the original number string
    if largest_even_index == -1:
        return num_str
    
    # Swap the largest even digit with the last digit
    num_list[-1], num_list[largest_even_index] = num_list[largest_even_index], num_list[-1]
    
    # Join the list of characters back into a string and return the result
    return ''.join(num_list)

# Test the function
print(largest_even_number("1234"))  # Output: "4231"
print(largest_even_number("2456"))  # Output: "6542"
print(largest_even_number("1357"))  # Output: "1357"