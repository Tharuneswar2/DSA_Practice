def splitArray(nums, m):
    def canSplit(max_sum):
        # Initialize the current sum and the number of splits
        curr_sum, splits = 0, 1
        for num in nums:
            # If the current sum plus the current number exceeds the max sum
            if curr_sum + num > max_sum:
                # Increment the number of splits and reset the current sum
                splits += 1
                curr_sum = num
            else:
                # Otherwise, add the current number to the current sum
                curr_sum += num
        # Return True if the number of splits is less than or equal to m
        return splits <= m

    # Initialize the low and high values for the binary search
    low, high = max(nums), sum(nums)
    while low < high:
        # Calculate the mid value
        mid = (low + high) // 2
        # If we can split the array with the mid value
        if canSplit(mid):
            # Update the high value
            high = mid
        else:
            # Otherwise, update the low value
            low = mid + 1
    # Return the minimum sum
    return low

# Example usage:
nums = [7, 2, 5, 10, 8]
m = 2
print(splitArray(nums, m))  # Output: 18