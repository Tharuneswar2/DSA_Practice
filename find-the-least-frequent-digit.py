def find_least_frequent_digit(s):
    # Create a dictionary to store the frequency of each digit
    digit_frequency = {}
    
    # Iterate over the string
    for char in s:
        # Check if the character is a digit
        if char.isdigit():
            # If the digit is already in the dictionary, increment its count
            if char in digit_frequency:
                digit_frequency[char] += 1
            # If the digit is not in the dictionary, add it with a count of 1
            else:
                digit_frequency[char] = 1
                
    # If the dictionary is empty (i.e., no digits were found), return None
    if not digit_frequency:
        return None
    
    # Find the digit with the minimum frequency
    least_frequent_digit = min(digit_frequency, key=digit_frequency.get)
    
    return least_frequent_digit

# Test the function
print(find_least_frequent_digit("abc123def456"))  # Output: '1'
print(find_least_frequent_digit("abcdef"))  # Output: None