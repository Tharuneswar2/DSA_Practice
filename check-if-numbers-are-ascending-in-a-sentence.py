def are_numbers_ascending(s: str) -> bool:
    # Split the input string into words
    words = s.split()
    
    # Initialize the previous number to negative infinity
    prev_num = float('-inf')
    
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
    
    # If we have checked all numbers and haven't returned False, return True
    return True