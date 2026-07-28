# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def smallestStableIndex(arr):
    # Create a copy of the input array and sort it
    sorted_arr = sorted(arr)
    
    # Initialize an empty dictionary to store the indices of elements in the sorted array
    index_map = {}
    
    # Populate the index map with the indices of elements in the sorted array
    for i, num in enumerate(sorted_arr):
        if num not in index_map:
            index_map[num] = [i]
        else:
            index_map[num].append(i)
    
    # Initialize the result variable to store the smallest stable index
    result = float('inf')
    
    # Iterate over the input array
    for i, num in enumerate(arr):
        # Get the indices of the current element in the sorted array
        indices = index_map[num]
        
        # Find the smallest index that is greater than or equal to the current index
        idx = next((j for j in indices if j >= i), None)
        
        # If such an index is found, update the result
        if idx is not None:
            result = min(result, idx)
    
    # Return the smallest stable index
    return result