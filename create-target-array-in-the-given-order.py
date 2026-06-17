def createTargetArray(nums, index):
    # Initialize an empty list to store the target array
    target = []
    
    # Iterate over the given list of numbers and their indices
    for num, idx in zip(nums, index):
        # Insert the number at the specified index in the target array
        # If the index is out of range, append the number to the end
        target.insert(idx, num)
    
    # Return the target array
    return target