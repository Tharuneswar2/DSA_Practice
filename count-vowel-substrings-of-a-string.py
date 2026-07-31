# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def count_vowel_substrings(word):
    # Initialize count of vowel substrings to 0
    count = 0
    
    # Define vowels for easy reference
    vowels = set('aeiou')
    
    # Iterate over the string with two nested loops to generate all substrings
    for i in range(len(word)):
        # Initialize a set to store unique vowels in the current substring
        vowel_set = set()
        
        # Initialize a flag to indicate if the current substring contains all unique vowels
        all_unique_vowels = True
        
        for j in range(i, len(word)):
            # If the current character is not a vowel, break the inner loop
            if word[j] not in vowels:
                break
            
            # Add the current vowel to the set
            vowel_set.add(word[j])
            
            # If the number of unique vowels is more than the length of the substring, 
            # it means the substring contains duplicate vowels, so set the flag to False
            if len(vowel_set) != j - i + 1:
                all_unique_vowels = False
            
            # If the substring contains all unique vowels and its length is equal to the number of unique vowels, 
            # increment the count of vowel substrings
            if all_unique_vowels and len(vowel_set) == 5:
                count += 1
                
    # Return the count of vowel substrings
    return count