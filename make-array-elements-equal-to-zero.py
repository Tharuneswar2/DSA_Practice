def make_equal_to_zero(nums):
    # Create a dictionary to store the frequency of each number
    freq_dict = {}
    
    # Populate the frequency dictionary
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Find the number with the maximum frequency
    max_freq_num = max(freq_dict, key=freq_dict.get)
    
    # Calculate the minimum number of operations required
    min_operations = len(nums) - freq_dict[max_freq_num]
    
    return min_operations

# Test the function
nums = [1, 2, 2, 3, 3, 3]
print(make_equal_to_zero(nums))  # Output: 3