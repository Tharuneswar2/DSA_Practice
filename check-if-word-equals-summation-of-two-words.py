def is_sum_equal(first_word, second_word, target_word):
    # Convert words to numbers by mapping each letter to its corresponding number (a=1, b=2, ..., z=26)
    def word_to_num(word):
        return sum(ord(char) - 96 for char in word)

    # Calculate the sum of the first two words
    sum_of_first_two_words = word_to_num(first_word) + word_to_num(second_word)

    # Check if the sum equals the target word
    return sum_of_first_two_words == word_to_num(target_word)

# Test the function
print(is_sum_equal("aaa", "a", "aab"))  # True
print(is_sum_equal("aaa", "a", "aaaa"))  # False