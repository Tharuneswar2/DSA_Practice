# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def kLengthApart(nums, k):
    # Initialize the index of the last seen 1
    last_seen = -k - 1
    
    # Iterate over the list with index and value
    for i, num in enumerate(nums):
        # If the current number is 1
        if num == 1:
            # If the distance between the current 1 and the last seen 1 is less than k, return False
            if i - last_seen < k:
                return False
            # Update the index of the last seen 1
            last_seen = i
    
    # If we have iterated over the entire list and haven't returned False, return True
    return True