def check_distances(s, distance):
    # Create a dictionary to store the indices of each character
    char_indices = {}
    
    # Iterate over the string to store the indices of each character
    for i, char in enumerate(s):
        if char in char_indices:
            # If the character is already in the dictionary, append the current index
            char_indices[char].append(i)
        else:
            # If the character is not in the dictionary, add it with the current index
            char_indices[char] = [i]
    
    # Iterate over the dictionary to check the distances between the same letters
    for indices in char_indices.values():
        # If there are less than two indices, skip this character
        if len(indices) < 2:
            continue
        
        # Iterate over the indices to check the distances
        for i in range(len(indices) - 1):
            # If the distance between two indices is not equal to the given distance, return False
            if indices[i + 1] - indices[i] != distance:
                return False
    
    # If all distances are equal to the given distance, return True
    return True