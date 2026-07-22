# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maxEqualScore(nums, k):
    # Initialize a hashmap to store the frequency of each number
    freq_map = {}
    
    # Initialize the maximum frequency and the result
    max_freq = 0
    res = 0
    
    # Iterate over the array with a sliding window of size k
    for i in range(len(nums)):
        # Add the current number to the frequency map
        freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1
        
        # If the window size is greater than k, remove the leftmost number
        if i >= k:
            freq_map[nums[i - k]] -= 1
            if freq_map[nums[i - k]] == 0:
                del freq_map[nums[i - k]]
        
        # Update the maximum frequency
        max_freq = max(max_freq, max(freq_map.values()))
        
        # Update the result
        res = max(res, max_freq * (i + 1 - k + 1))
    
    return res