def reorder_spaces(text):
    # Count the total number of spaces in the text
    total_spaces = text.count(' ')

    # Split the text into words
    words = text.split()

    # If there's only one word, return the text with all spaces appended at the end
    if len(words) == 1:
        return words[0] + ' ' * total_spaces

    # Calculate the number of spaces to be added between words
    spaces_between = total_spaces // (len(words) - 1)

    # Calculate the number of extra spaces
    extra_spaces = total_spaces % (len(words) - 1)

    # Initialize the result string
    result = ''

    # Add words to the result string with the calculated number of spaces in between
    for i in range(len(words)):
        result += words[i]
        if i < len(words) - 1:
            result += ' ' * spaces_between
        # Add an extra space if there are remaining spaces
        if i < extra_spaces:
            result += ' '

    return result