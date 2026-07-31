# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def maxNumberOfBalloons(text: str) -> int:
    # Create a dictionary to store the frequency of each character in the string 'balloon'
    balloon_freq = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
    
    # Iterate over each character in the string 'text'
    for char in text:
        # If the character is in the 'balloon_freq' dictionary, increment its frequency
        if char in balloon_freq:
            balloon_freq[char] += 1
    
    # Since 'l' and 'o' appear twice in the string 'balloon', we need to divide their frequencies by 2
    balloon_freq['l'] //= 2
    balloon_freq['o'] //= 2
    
    # The maximum number of 'balloon' strings that can be formed is the minimum frequency of all characters
    return min(balloon_freq.values())