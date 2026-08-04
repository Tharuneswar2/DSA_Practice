# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countGoodSubstrings(s):
    # Initialize count to store the number of substrings of size three with distinct characters
    count = 0
    
    # Iterate over the string from index 0 to the third last character
    for i in range(len(s) - 2):
        # Extract the substring of size three
        substring = s[i:i+3]
        
        # Check if all characters in the substring are distinct
        if len(set(substring)) == 3:
            # If distinct, increment the count
            count += 1
    
    # Return the count of substrings of size three with distinct characters
    return count