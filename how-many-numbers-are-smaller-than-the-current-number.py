# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def smallerNumbersThanCurrent(nums):
    # Create a copy of the input list and sort it in ascending order
    sorted_nums = sorted(nums)
    
    # Initialize an empty dictionary to store the count of smaller numbers for each number
    count_dict = {}
    
    # Iterate over the sorted list to populate the dictionary
    for i, num in enumerate(sorted_nums):
        # If the number is not already in the dictionary, add it with its count
        if num not in count_dict:
            # The count of smaller numbers is the index of the current number in the sorted list
            count_dict[num] = i
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list to construct the result
    for num in nums:
        # Append the count of smaller numbers for the current number to the result
        result.append(count_dict[num])
    
    # Return the result
    return result