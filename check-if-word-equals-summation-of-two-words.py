# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def isSumEqual(firstWord, secondWord, targetWord):
    # Define a helper function to convert a word to a number
    def word_to_num(word):
        # Initialize the result to 0
        num = 0
        # Iterate over each character in the word
        for char in word:
            # Convert the character to its corresponding digit (a=0, b=1, ..., j=9)
            digit = ord(char) - ord('a')
            # Append the digit to the result
            num = num * 10 + digit
        # Return the result
        return num

    # Convert the first word to a number
    first_num = word_to_num(firstWord)
    # Convert the second word to a number
    second_num = word_to_num(secondWord)
    # Convert the target word to a number
    target_num = word_to_num(targetWord)

    # Check if the sum of the first two numbers equals the target number
    return first_num + second_num == target_num