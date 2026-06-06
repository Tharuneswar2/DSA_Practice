def count_vowel_substrings(word):
    # Initialize count of vowel substrings
    count = 0
    
    # Define vowels
    vowels = set('aeiou')
    
    # Iterate over the string
    for i in range(len(word)):
        # Initialize a set to store unique vowels in the current substring
        vowel_set = set()
        
        # Iterate over the substring starting at the current position
        for j in range(i, len(word)):
            # If the character is not a vowel, break the loop
            if word[j] not in vowels:
                break
                
            # Add the vowel to the set
            vowel_set.add(word[j])
            
            # If the number of unique vowels is equal to the length of the substring,
            # it's a vowel substring, so increment the count
            if len(vowel_set) == j - i + 1:
                count += 1
                
    return count