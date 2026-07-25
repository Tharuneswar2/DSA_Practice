# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maximumCount(nums):
    # Initialize two pointers, one at the start and one at the end of the array
    pos = 0 
    neg = len(nums) - 1
    
    # Initialize counters for positive and negative numbers
    pos_count = 0
    neg_count = 0
    
    # Traverse the array from both ends
    while pos <= neg:
        # If the current number is positive, increment the positive counter and move the positive pointer
        if nums[pos] > 0:
            pos_count += 1
            pos += 1
        # If the current number is negative, increment the negative counter and move the negative pointer
        elif nums[neg] < 0:
            neg_count += 1
            neg -= 1
        # If the current numbers are both zero or one is zero and the other is not, move both pointers
        else:
            pos += 1
            neg -= 1
    
    # Return the maximum count
    return max(pos_count, neg_count)