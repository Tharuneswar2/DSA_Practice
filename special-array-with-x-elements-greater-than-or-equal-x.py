def specialArray(nums):
    # Create a frequency map to store the frequency of each number in the array
    freq_map = {}
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    # Initialize the variable to store the result
    result = -1

    # Iterate over the range from 1 to the length of the array plus one
    for x in range(1, len(nums) + 1):
        # Initialize the count of numbers greater than or equal to x
        count = 0
        # Iterate over the frequency map
        for num, freq in freq_map.items():
            # If the number is greater than or equal to x, add its frequency to the count
            if num >= x:
                count += freq
        # If the count is equal to x, update the result
        if count == x:
            result = x

    # Return the result
    return result