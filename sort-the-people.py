def sortPeople(names, heights):
    # Combine names and heights into a list of tuples
    name_height_pairs = list(zip(names, heights))
    
    # Sort the list of tuples based on the heights in descending order
    # If two people have the same height, sort them based on their names in ascending order
    sorted_pairs = sorted(name_height_pairs, key=lambda x: (-x[1], x[0]))
    
    # Separate the sorted names from the heights
    sorted_names = [pair[0] for pair in sorted_pairs]
    
    return sorted_names