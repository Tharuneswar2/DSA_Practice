def destCity(paths):
    # Create a set of all cities that are the origin of a path
    origins = set(path[0] for path in paths)
    
    # Iterate over all paths to find the city that is not an origin
    for path in paths:
        # If the destination city is not in the set of origins, it's the destination city
        if path[1] not in origins:
            return path[1]