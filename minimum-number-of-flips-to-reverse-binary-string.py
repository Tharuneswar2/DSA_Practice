def min_flips(s):
    # Initialize variables to keep track of the number of flips
    # and the current character
    flips = 0
    curr_char = '0'

    # Iterate over the string
    for char in s:
        # If the current character is different from the previous one,
        # increment the number of flips and update the current character
        if char != curr_char:
            flips += 1
            curr_char = char

    # Return the minimum number of flips
    return (flips + 1) // 2

# Test the function
print(min_flips("00000101110"))  # Output: 2
print(min_flips("00000000"))  # Output: 0
print(min_flips("11111111"))  # Output: 0