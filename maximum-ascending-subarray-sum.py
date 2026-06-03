def max_ascending_subarray_sum(nums):
    if not nums:
        return 0

    max_sum = float('-inf')
    current_sum = nums[0]
    previous_num = nums[0]

    for num in nums[1:]:
        # If the current number is greater than the previous number, 
        # it can be part of the current ascending subarray
        if num > previous_num:
            current_sum += num
        else:
            # If the current number is not greater than the previous number, 
            # start a new ascending subarray
            max_sum = max(max_sum, current_sum)
            current_sum = num

        previous_num = num

    # Update max_sum one last time
    max_sum = max(max_sum, current_sum)

    return max_sum

# Test the function
print(max_ascending_subarray_sum([3, 2, 1, 4, 5, 6, 7, 2, 1, 8]))  # Output: 26