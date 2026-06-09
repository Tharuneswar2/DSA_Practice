def findLongestBalancedSubstring(s):
    # Initialize variables to keep track of the longest balanced substring and its length
    max_len = 0
    max_substr = ""

    # Initialize variables to keep track of the current balanced substring and its length
    curr_len = 0
    curr_substr = ""

    # Initialize variables to keep track of the count of 0s and 1s in the current substring
    zeros = 0
    ones = 0

    # Iterate over the string
    for char in s:
        # If the character is '0', increment the count of zeros
        if char == '0':
            zeros += 1
        # If the character is '1', increment the count of ones
        else:
            ones += 1

        # If the counts of zeros and ones are equal, it means we have a balanced substring
        if zeros == ones:
            # Update the length of the current substring
            curr_len = zeros + ones
            # Update the current substring
            curr_substr = s[s.index(char) - curr_len + 1:s.index(char) + 1]

            # If the length of the current substring is greater than the maximum length, update the maximum length and substring
            if curr_len > max_len:
                max_len = curr_len
                max_substr = curr_substr

        # If the counts of zeros and ones are not equal, reset the current substring and its length
        else:
            zeros = 0
            ones = 0
            curr_len = 0
            curr_substr = ""

    # Return the longest balanced substring
    return max_substr

# Test the function
print(findLongestBalancedSubstring("01000111"))