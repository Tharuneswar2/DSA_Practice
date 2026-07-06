def canBeIncreasing(nums):
    # Initialize a variable to track if we have removed an element
    removed = False
    
    # Iterate over the array
    for i in range(1, len(nums)):
        # If the current element is not greater than the previous one
        if nums[i] <= nums[i - 1]:
            # If we have already removed an element, return False
            if removed:
                return False
            # Otherwise, mark that we have removed an element
            removed = True
            
            # Check if removing the current element or the previous one makes the array strictly increasing
            if i == 1 or nums[i] > nums[i - 2]:
                # If removing the current element makes the array strictly increasing, continue
                continue
            else:
                # Otherwise, remove the previous element
                nums[i - 1] = nums[i]
    
    # If we have iterated over the entire array and removed at most one element, return True
    return True