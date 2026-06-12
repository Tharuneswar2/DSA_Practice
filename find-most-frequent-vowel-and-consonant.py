def most_frequent_vowel_and_consonant(input_string):
    # Convert the input string to lowercase for case-insensitive comparison
    input_string = input_string.lower()
    
    # Initialize dictionaries to store the frequency of vowels and consonants
    vowel_frequency = {}
    consonant_frequency = {}
    
    # Define the set of vowels
    vowels = set('aeiou')
    
    # Iterate over each character in the input string
    for char in input_string:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Check if the character is a vowel
            if char in vowels:
                # Increment the frequency of the vowel in the vowel_frequency dictionary
                vowel_frequency[char] = vowel_frequency.get(char, 0) + 1
            else:
                # Increment the frequency of the consonant in the consonant_frequency dictionary
                consonant_frequency[char] = consonant_frequency.get(char, 0) + 1
    
    # Find the most frequent vowel
    most_frequent_vowel = max(vowel_frequency, key=vowel_frequency.get, default=None)
    
    # Find the most frequent consonant
    most_frequent_consonant = max(consonant_frequency, key=consonant_frequency.get, default=None)
    
    return most_frequent_vowel, most_frequent_consonant

# Example usage
input_string = "Hello, World!"
most_frequent_vowel, most_frequent_consonant = most_frequent_vowel_and_consonant(input_string)
print("Most Frequent Vowel:", most_frequent_vowel)
print("Most Frequent Consonant:", most_frequent_consonant)