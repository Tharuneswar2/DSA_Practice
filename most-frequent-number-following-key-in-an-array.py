# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def mostFrequent(nums, key):
    # Create a dictionary to store the frequency of each number following the key
    freq_dict = {}
    
    # Iterate over the list of numbers
    for i in range(len(nums) - 1):
        # Check if the current number is the key
        if nums[i] == key:
            # If the key is found, increment the frequency of the next number in the dictionary
            freq_dict[nums[i + 1]] = freq_dict.get(nums[i + 1], 0) + 1
    
    # Find the number with the maximum frequency
    max_freq = max(freq_dict.values())
    
    # Find all numbers with the maximum frequency
    max_freq_nums = [num for num, freq in freq_dict.items() if freq == max_freq]
    
    # Return the smallest number with the maximum frequency
    return min(max_freq_nums)