# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def createTargetArray(nums, index):
    # Initialize an empty list to store the target array
    target = []
    
    # Iterate over the given list of numbers and their indices
    for num, idx in zip(nums, index):
        # Insert the number at the specified index in the target array
        # The insert operation in Python lists is O(n) because all elements after the insertion point need to be shifted
        # However, since we are inserting at most n elements, the overall time complexity remains O(n)
        target.insert(idx, num)
    
    # Return the constructed target array
    return target