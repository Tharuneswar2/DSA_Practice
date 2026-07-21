# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def dominantIndex(nums):
    # Check if the input list is empty
    if not nums:
        return -1
    
    # Find the maximum number in the list
    max_num = max(nums)
    
    # Find the index of the maximum number
    max_index = nums.index(max_num)
    
    # Iterate over the list to check if all other numbers are less than or equal to half of the maximum number
    for i, num in enumerate(nums):
        # Skip the maximum number itself
        if i == max_index:
            continue
        # If any number is greater than half of the maximum number, return -1
        if num > max_num / 2:
            return -1
    
    # If all other numbers are less than or equal to half of the maximum number, return the index of the maximum number
    return max_index