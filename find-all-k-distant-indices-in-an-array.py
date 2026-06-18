def findKDistantIndices(nums, k):
    # Initialize an empty list to store the indices
    indices = []
    
    # Initialize a variable to store the previous index
    prev_index = -1
    
    # Iterate over the list of numbers
    for i, num in enumerate(nums):
        # If the current number is 1
        if num == 1:
            # If the previous index is -1 or the difference between the current index and the previous index is greater than k
            if prev_index == -1 or i - prev_index > k:
                # Add all indices from the previous index + k to the current index to the list of indices
                indices.extend(range(prev_index + k + 1, i + 1))
            # Update the previous index
            prev_index = i
    
    # If the last number is 1
    if nums[-1] == 1:
        # Add all indices from the previous index + k to the end of the list to the list of indices
        indices.extend(range(prev_index + k + 1, len(nums)))
    
    # Return the list of indices
    return indices