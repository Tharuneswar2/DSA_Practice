# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def areNumbersAscending(s: str) -> bool:
    # Initialize the previous number to 0, assuming the first number in the sentence will be greater than 0
    prev_num = 0
    
    # Split the input string into words
    words = s.split()
    
    # Iterate over each word in the sentence
    for word in words:
        # Check if the word is a digit
        if word.isdigit():
            # Convert the word to an integer
            num = int(word)
            
            # If the current number is not greater than the previous number, return False
            if num <= prev_num:
                return False
            
            # Update the previous number
            prev_num = num
    
    # If we have iterated over all the numbers in the sentence and they are in ascending order, return True
    return True