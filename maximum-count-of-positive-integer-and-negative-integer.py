def maximumCount(nums):
    # Initialize counters for positive and negative integers
    positive_count = 0
    negative_count = 0
    
    # Iterate through the list of integers
    for num in nums:
        # If the number is positive, increment the positive counter
        if num > 0:
            positive_count += 1
        # If the number is negative, increment the negative counter
        elif num < 0:
            negative_count += 1
    
    # Return the maximum count between positive and negative integers
    return max(positive_count, negative_count)