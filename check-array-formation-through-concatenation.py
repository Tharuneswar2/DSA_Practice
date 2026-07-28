# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def canFormArray(arr, pieces):
    # Create a hashmap to store the pieces for efficient lookups
    piece_map = {piece[0]: piece for piece in pieces}
    
    # Initialize an empty result array
    result = []
    
    # Iterate over the input array
    i = 0
    while i < len(arr):
        # If the current element is the start of a piece, append the entire piece to the result
        if arr[i] in piece_map:
            result.extend(piece_map[arr[i]])
            # Move the index forward by the length of the piece
            i += len(piece_map[arr[i]])
        else:
            # If the current element is not the start of a piece, return False
            return False
    
    # If we've iterated over the entire array and the result matches the input array, return True
    return result == arr