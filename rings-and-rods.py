def countPoints(rings):
    # Initialize a dictionary to store the count of each color on each rod
    rod_counts = {}
    
    # Iterate over the rings string in steps of 2
    for i in range(0, len(rings), 2):
        # Get the color and rod number
        color = rings[i]
        rod = int(rings[i+1])
        
        # If the rod is not in the dictionary, add it
        if rod not in rod_counts:
            rod_counts[rod] = set()
        
        # Add the color to the set of colors on the rod
        rod_counts[rod].add(color)
    
    # Initialize a counter for the number of rods with 3 colors
    count = 0
    
    # Iterate over the rods
    for rod in rod_counts:
        # If the rod has 3 colors, increment the counter
        if len(rod_counts[rod]) == 3:
            count += 1
    
    # Return the count
    return count

# Test the function
print(countPoints("B0B6G0R6R0R6G9"))