# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def findKDistantIndices(nums, k):
    # Initialize an empty list to store the indices of elements that are k-distant from the given array
    result = []
    
    # Initialize a variable to keep track of the previous index
    prev_index = -1
    
    # Iterate over the array
    for i in range(len(nums)):
        # Check if the current element is k-distant from the previous index
        if i - prev_index > k:
            # If it is, update the previous index and add the current index to the result
            prev_index = i
            result.append(i)
    
    # Return the list of k-distant indices
    return result