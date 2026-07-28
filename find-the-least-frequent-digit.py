# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def least_frequent_digit(s):
    # Create a dictionary to store the frequency of each digit
    digit_freq = {}
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a digit
        if char.isdigit():
            # If the digit is already in the dictionary, increment its count
            if char in digit_freq:
                digit_freq[char] += 1
            # If the digit is not in the dictionary, add it with a count of 1
            else:
                digit_freq[char] = 1
                
    # If the string does not contain any digits, return None
    if not digit_freq:
        return None
    
    # Find the digit with the minimum frequency
    least_frequent = min(digit_freq, key=digit_freq.get)
    
    # Return the least frequent digit
    return least_frequent