# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def find_most_frequent_vowel_and_consonant(input_string):
    # Initialize dictionaries to store the frequency of vowels and consonants
    vowel_frequency = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    consonant_frequency = {}

    # Iterate over each character in the input string
    for char in input_string.lower():
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Check if the character is a vowel
            if char in vowel_frequency:
                # Increment the frequency of the vowel
                vowel_frequency[char] += 1
            else:
                # If the character is a consonant, increment its frequency
                consonant_frequency[char] = consonant_frequency.get(char, 0) + 1

    # Find the most frequent vowel
    most_frequent_vowel = max(vowel_frequency, key=vowel_frequency.get)

    # Find the most frequent consonant
    most_frequent_consonant = max(consonant_frequency, key=consonant_frequency.get)

    # Return the most frequent vowel and consonant
    return most_frequent_vowel, most_frequent_consonant

# Test the function
input_string = "Hello World"
most_frequent_vowel, most_frequent_consonant = find_most_frequent_vowel_and_consonant(input_string)
print("Most frequent vowel:", most_frequent_vowel)
print("Most frequent consonant:", most_frequent_consonant)