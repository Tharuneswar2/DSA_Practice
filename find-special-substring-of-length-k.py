def find_substring(s, k):
    # Initialize an empty list to store the result
    result = []

    # Iterate over the string with a sliding window of size k
    for i in range(len(s) - k + 1):
        # Extract the substring of length k
        substring = s[i:i+k]

        # Check if the substring has all unique characters
        if len(set(substring)) == k:
            # If all characters are unique, add the substring to the result
            result.append(substring)

    # Return the result
    return result

# Test the function
print(find_substring("abcabc", 2))