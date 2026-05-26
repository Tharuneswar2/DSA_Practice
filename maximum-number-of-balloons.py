def maxNumberOfBalloons(text):
    # Create a dictionary to store the frequency of each character in 'balloon'
    freq = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
    
    # Iterate over each character in the input text
    for char in text:
        # If the character is in 'balloon', increment its frequency
        if char in freq:
            freq[char] += 1
    
    # Since 'l' and 'o' appear twice in 'balloon', divide their frequencies by 2
    freq['l'] //= 2
    freq['o'] //= 2
    
    # The maximum number of 'balloon' that can be formed is the minimum frequency of its characters
    return min(freq.values())