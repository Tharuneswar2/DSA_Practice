def count_commas_in_range(s, start, end):
    # Check if the start and end indices are valid
    if start < 0 or end > len(s) or start > end:
        return "Invalid range"

    # Slice the string to get the substring in the given range
    substring = s[start:end+1]

    # Initialize a counter for commas
    comma_count = 0

    # Iterate over each character in the substring
    for char in substring:
        # Check if the character is a comma
        if char == ',':
            # If it's a comma, increment the counter
            comma_count += 1

    # Return the count of commas
    return comma_count

# Alternatively, you can use the count method of Python strings
def count_commas_in_range_alternative(s, start, end):
    # Check if the start and end indices are valid
    if start < 0 or end > len(s) or start > end:
        return "Invalid range"

    # Slice the string to get the substring in the given range
    substring = s[start:end+1]

    # Use the count method to count the commas
    return substring.count(',')

# Test the functions
print(count_commas_in_range("hello, world, this, is, a, test", 0, 20))
print(count_commas_in_range_alternative("hello, world, this, is, a, test", 0, 20))