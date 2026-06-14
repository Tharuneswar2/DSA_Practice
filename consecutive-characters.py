def maxConsecutiveChars(s: str) -> int:
    # Initialize variables to store the maximum count and the current count
    max_count = 0
    current_count = 1

    # Iterate over the string from the second character to the end
    for i in range(1, len(s)):
        # If the current character is the same as the previous one, increment the current count
        if s[i] == s[i - 1]:
            current_count += 1
        # If the current character is different from the previous one, update the max count if necessary and reset the current count
        else:
            max_count = max(max_count, current_count)
            current_count = 1

    # Update the max count one last time after the loop ends
    max_count = max(max_count, current_count)

    return max_count