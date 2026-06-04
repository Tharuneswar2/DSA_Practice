def canFormArray(arr, pieces):
    # Create a hashmap to store the pieces for O(1) lookup
    piece_map = {tuple(piece): piece for piece in pieces}
    
    # Initialize an empty result array
    result = []
    
    # Iterate over the input array
    i = 0
    while i < len(arr):
        # Check if the current subarray is in the piece map
        for j in range(i + 1, len(arr) + 1):
            subarray = tuple(arr[i:j])
            if subarray in piece_map:
                # If it is, append it to the result array and move the index
                result.append(piece_map[subarray])
                i = j
                break
        else:
            # If no matching piece is found, return False
            return False
    
    # If we've iterated over the entire array, return True
    return True