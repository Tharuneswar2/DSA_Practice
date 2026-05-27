def max_repeating_substring(s):
    # Initialize variables to store the maximum repeating substring and its count
    max_substring = ""
    max_count = 0

    # Iterate over the string with two nested loops to generate all possible substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            # Initialize a counter to store the count of the current substring
            count = 0
            # Initialize a pointer to the start of the string
            k = 0
            # Iterate over the string to count the occurrences of the current substring
            while k < len(s):
                # Check if the substring matches the string at the current position
                if s[k:].startswith(substring):
                    # If it matches, increment the counter and move the pointer
                    count += 1
                    k += len(substring)
                else:
                    # If it doesn't match, move the pointer
                    k += 1
            # Update the maximum repeating substring and its count if necessary
            if count > max_count:
                max_count = count
                max_substring = substring

    return max_substring, max_count

# Example usage:
s = "ababcab"
max_substring, max_count = max_repeating_substring(s)
print(f"Maximum repeating substring: {max_substring}")
print(f"Maximum count: {max_count}")