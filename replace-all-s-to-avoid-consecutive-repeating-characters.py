def replace_question_marks(s):
    # Initialize an empty string to store the result
    result = ""

    # Iterate over the input string
    for i in range(len(s)):
        # If the character is a question mark
        if s[i] == '?':
            # If it's the first character or the previous character is not the same as the next character
            if i == 0 or (i < len(s) - 1 and s[i-1] != s[i+1]):
                # Replace the question mark with 'a'
                result += 'a'
            else:
                # Replace the question mark with 'b'
                result += 'b'
        else:
            # If the character is not a question mark, just append it to the result
            result += s[i]

    return result

def replace_question_marks_alternative(s):
    # Initialize an empty string to store the result
    result = ""

    # Initialize the previous character
    prev_char = ''

    # Iterate over the input string
    for char in s:
        # If the character is a question mark
        if char == '?':
            # If the previous character is 'a', replace the question mark with 'b'
            if prev_char == 'a':
                result += 'b'
            # If the previous character is 'b', replace the question mark with 'a'
            elif prev_char == 'b':
                result += 'a'
            # If the previous character is not 'a' or 'b', replace the question mark with 'a'
            else:
                result += 'a'
        else:
            # If the character is not a question mark, just append it to the result
            result += char

        # Update the previous character
        prev_char = result[-1]

    return result