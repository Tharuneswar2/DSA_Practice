# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def destCity(paths):
    # Create a set to store all the cities that are the starting point of a path
    start_cities = set()
    
    # Iterate over each path in the list of paths
    for path in paths:
        # Add the starting city of the current path to the set of start cities
        start_cities.add(path[0])
    
    # Iterate over each path in the list of paths again
    for path in paths:
        # If the destination city of the current path is not in the set of start cities, 
        # it means this city is not the starting point of any path, so it's the destination city
        if path[1] not in start_cities:
            # Return the destination city
            return path[1]