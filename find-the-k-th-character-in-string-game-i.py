# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def findKthCharacter(s, k):
    # Initialize an empty string to store the concatenated string
    concatenated_str = ""
    
    # Loop through the string s
    for char in s:
        # Concatenate the string with itself and the character
        concatenated_str += char * (len(concatenated_str) + 1)
        
        # If the length of the concatenated string is greater than or equal to k
        if len(concatenated_str) >= k:
            # Return the character at index k - 1
            return concatenated_str[k - 1]