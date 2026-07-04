def minMaxGame(nums):
    # Base case: if the length of the array is 1, return the only element
    if len(nums) == 1:
        return nums[0]

    # Initialize a new array to store the results of the subproblems
    new_nums = []

    # Iterate over the array in steps of 2
    for i in range(0, len(nums), 2):
        # Calculate the minimum and maximum of the current pair
        min_val = min(nums[i], nums[i+1])
        max_val = max(nums[i], nums[i+1])

        # Append the minimum and maximum to the new array
        new_nums.append(min_val)
        new_nums.append(max_val)

    # If the length of the new array is even, recursively call the function
    if len(new_nums) % 2 == 0:
        return minMaxGame(new_nums)
    # If the length of the new array is odd, return the minimum of the array
    else:
        return min(new_nums)

# Test the function
print(minMaxGame([1,3,5,2,4,8,2,2]))  # Output: 1