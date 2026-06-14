def smallerNumbersThanCurrent(nums):
    # Create a sorted copy of the input list to maintain the original order
    sorted_nums = sorted(nums)
    
    # Initialize an empty dictionary to store the count of smaller numbers
    smaller_count = {}
    
    # Iterate over the sorted list to populate the dictionary
    for i, num in enumerate(sorted_nums):
        # If the number is not already in the dictionary, add it with its index
        if num not in smaller_count:
            smaller_count[num] = i
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list to construct the result
    for num in nums:
        # Append the count of smaller numbers for the current number to the result
        result.append(smaller_count[num])
    
    # Return the result
    return result