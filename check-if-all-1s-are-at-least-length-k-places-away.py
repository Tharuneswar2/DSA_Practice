def kLengthApart(nums, k):
    # Initialize the previous index of 1 to -k-1, so the first 1 will be at least k places away
    prev = -k - 1
    
    # Iterate over the list with index and value
    for i, num in enumerate(nums):
        # If the current number is 1
        if num == 1:
            # If the difference between the current index and the previous index is less than k, return False
            if i - prev < k:
                return False
            # Update the previous index
            prev = i
    
    # If we have iterated over the entire list and haven't returned False, all 1's are at least k places away
    return True