# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def isTonic(nums):
    # Initialize a variable to track the trend of the sequence
    trend = None
    
    # Iterate over the sequence from the second element to the end
    for i in range(1, len(nums)):
        # If the current element is greater than the previous one, the trend is increasing
        if nums[i] > nums[i - 1]:
            # If the trend was previously decreasing or None, update the trend
            if trend == False or trend is None:
                trend = True
            # If the trend was previously increasing, continue
            else:
                continue
        # If the current element is less than the previous one, the trend is decreasing
        elif nums[i] < nums[i - 1]:
            # If the trend was previously increasing or None, update the trend
            if trend == True or trend is None:
                trend = False
            # If the trend was previously decreasing, continue
            else:
                continue
        # If the current element is equal to the previous one, the sequence is not tonic
        else:
            return False
    
    # If the sequence has passed the checks, it is tonic
    return True