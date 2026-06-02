def count_special_characters(s):
    # Initialize a counter variable to store the count of special characters
    count = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is not alphanumeric (i.e., it's a special character)
        if not char.isalnum():
            # If it's a special character, increment the counter
            count += 1
    
    # Return the total count of special characters
    return count

# Test the function
print(count_special_characters("Hello, World!"))