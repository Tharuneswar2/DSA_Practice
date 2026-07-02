def first_palindromic_string(words):
    # Define a helper function to check if a string is a palindrome
    def is_palindrome(word):
        # Compare the word with its reverse
        return word == word[::-1]

    # Iterate over each word in the list
    for word in words:
        # Check if the word is a palindrome
        if is_palindrome(word):
            # If it is, return the word
            return word

    # If no palindromic string is found, return None
    return None

# Example usage:
words = ["hello", "world", "radar", "python"]
print(first_palindromic_string(words))  # Output: "radar"