# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def count_substrings(s, k):
    # Initialize count to store the number of substrings that satisfy the k-constraint
    count = 0
    
    # Iterate over the string with two nested loops to generate all possible substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            # Extract the current substring
            substring = s[i:j]
            
            # Initialize a dictionary to store the frequency of each character in the substring
            freq = {}
            
            # Iterate over the substring to count the frequency of each character
            for char in substring:
                # If the character is already in the dictionary, increment its count
                if char in freq:
                    freq[char] += 1
                # If the character is not in the dictionary, add it with a count of 1
                else:
                    freq[char] = 1
            
            # Check if the substring satisfies the k-constraint
            if len(freq) == k:
                # If the substring satisfies the k-constraint, increment the count
                count += 1
    
    # Return the total count of substrings that satisfy the k-constraint
    return count