# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def checkDistances(s, distance):
    # Create a dictionary to store the last seen index of each character
    last_seen = {}
    
    # Iterate over the string with the index and character
    for i, c in enumerate(s):
        # If the character is already in the dictionary
        if c in last_seen:
            # Calculate the distance between the current index and the last seen index
            dist = i - last_seen[c]
            # If the calculated distance does not match the given distance, return False
            if dist != distance[ord(c) - ord('a')]:
                return False
        # Update the last seen index of the character
        last_seen[c] = i
    
    # If we have checked all characters and their distances, return True
    return True