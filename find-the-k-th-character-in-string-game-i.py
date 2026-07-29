# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def findKthCharacter(s, k):
    # Initialize an empty string to store the concatenated string
    concatenated_str = ""
    
    # Loop through the string s
    for char in s:
        # Concatenate the character to the concatenated string
        concatenated_str += char
        
        # If the length of the concatenated string is equal to k, return the character
        if len(concatenated_str) == k:
            return char
        
        # If the length of the concatenated string is greater than k, 
        # it means the k-th character is in the concatenated string
        if len(concatenated_str) > k:
            # Return the k-th character in the concatenated string
            return concatenated_str[k-1]
            
    # If the length of the concatenated string is less than k, 
    # it means the k-th character is not in the concatenated string
    # So, we need to concatenate the string s to itself
    while len(concatenated_str) < k:
        # Concatenate the string s to the concatenated string
        concatenated_str += s
        
    # Return the k-th character in the concatenated string
    return concatenated_str[k-1]