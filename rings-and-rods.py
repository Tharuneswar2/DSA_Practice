# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def countPoints(rings):
    # Initialize a dictionary to store the count of each color on each rod
    rod_colors = {}
    
    # Iterate over the rings string in steps of 2
    for i in range(0, len(rings), 2):
        # Get the color and rod index
        color, rod = rings[i], int(rings[i+1])
        
        # If the rod is not in the dictionary, add it
        if rod not in rod_colors:
            rod_colors[rod] = set()
        
        # Add the color to the set of colors on the rod
        rod_colors[rod].add(color)
    
    # Initialize a counter for the number of rods with all three colors
    count = 0
    
    # Iterate over the rods and their colors
    for colors in rod_colors.values():
        # If a rod has all three colors, increment the counter
        if len(colors) == 3:
            count += 1
    
    # Return the count of rods with all three colors
    return count