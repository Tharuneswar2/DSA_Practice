def dominantIndex(nums):
    # Find the maximum number in the list
    max_num = max(nums)
    
    # Iterate over the list to check if all other numbers are less than or equal to half of the maximum number
    for num in nums:
        # If a number is greater than half of the maximum number and not the maximum number itself, return 0
        if num != max_num and num > max_num / 2:
            return 0
    
    # If no such number is found, return the index of the maximum number
    return nums.index(max_num)

# Test the function
print(dominantIndex([3, 6, 1, 0]))  # Output: 1
print(dominantIndex([1, 2, 3, 4]))  # Output: 0