# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def frequencySort(nums):
    # Create a dictionary to store the frequency of each number
    freq_dict = {}
    
    # Iterate over the input list to count the frequency of each number
    for num in nums:
        if num in freq_dict:
            # If the number is already in the dictionary, increment its count
            freq_dict[num] += 1
        else:
            # If the number is not in the dictionary, add it with a count of 1
            freq_dict[num] = 1
    
    # Sort the input list based on the frequency of each number and then its value
    # The sorted function in Python is stable, meaning that when multiple records have the same key, their original order is preserved
    return sorted(nums, key=lambda x: (freq_dict[x], x))