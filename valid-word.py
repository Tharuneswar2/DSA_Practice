def valid_word_abbreviation(word, abbr):
    # Initialize two pointers, one for the word and one for the abbreviation
    word_pointer = 0
    abbr_pointer = 0
    
    # Loop through the abbreviation
    while abbr_pointer < len(abbr):
        # If the current character in the abbreviation is a digit
        if abbr[abbr_pointer].isdigit():
            # Initialize a variable to store the number
            num = 0
            
            # Loop through the abbreviation until a non-digit character is found
            while abbr_pointer < len(abbr) and abbr[abbr_pointer].isdigit():
                # Multiply the current number by 10 and add the new digit
                num = num * 10 + int(abbr[abbr_pointer])
                abbr_pointer += 1
            
            # Move the word pointer by the number
            word_pointer += num
            
            # If the word pointer is beyond the length of the word, return False
            if word_pointer > len(word):
                return False
        
        # If the word pointer is equal to the length of the word, return False
        elif word_pointer == len(word):
            return False
        
        # If the current character in the word does not match the current character in the abbreviation, return False
        elif word[word_pointer] != abbr[abbr_pointer]:
            return False
        
        # Move both pointers
        word_pointer += 1
        abbr_pointer += 1
    
    # If the word pointer is not equal to the length of the word, return False
    if word_pointer != len(word):
        return False
    
    # If all checks pass, return True
    return True