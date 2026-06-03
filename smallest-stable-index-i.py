def smallestStableIndex(arr):
    # Create a copy of the array and sort it
    sorted_arr = sorted(arr)
    
    # Initialize an empty dictionary to store the indices of elements in the sorted array
    index_map = {}
    
    # Populate the index map
    for i, num in enumerate(sorted_arr):
        if num not in index_map:
            index_map[num] = [i]
        else:
            index_map[num].append(i)
    
    # Initialize the smallest stable index to infinity
    smallest_index = float('inf')
    
    # Iterate over the original array
    for i, num in enumerate(arr):
        # Get the indices of the current element in the sorted array
        indices = index_map[num]
        
        # Find the smallest index that is greater than or equal to the current index
        stable_index = next((index for index in indices if index >= i), None)
        
        # If a stable index is found, update the smallest stable index
        if stable_index is not None:
            smallest_index = min(smallest_index, stable_index)
    
    # Return the smallest stable index
    return smallest_index if smallest_index != float('inf') else -1