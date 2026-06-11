from collections import Counter

def rearrange_characters(s, target):
    # Count the frequency of characters in the string and the target
    s_count = Counter(s)
    target_count = Counter(target)

    # Initialize the result string
    result = ''

    # Iterate over the characters in the target string
    for char, count in target_count.items():
        # If the character is not in the string or its count is less than the target count, return an empty string
        if char not in s_count or s_count[char] < count:
            return ''

        # Add the character to the result string the specified number of times
        result += char * count

        # Subtract the count from the string's character count
        s_count[char] -= count

    # Add any remaining characters in the string to the result string
    for char, count in s_count.items():
        result += char * count

    return result