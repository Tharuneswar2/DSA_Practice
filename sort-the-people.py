# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def sortPeople(names, heights):
    # Combine the names and heights into a list of tuples
    name_height_pairs = list(zip(names, heights))
    
    # Sort the list of tuples based on the heights in descending order
    # The sorted function in Python is stable, meaning that when multiple records have the same key, their original order is preserved
    sorted_pairs = sorted(name_height_pairs, key=lambda x: x[1], reverse=True)
    
    # Separate the sorted names from the heights
    # The list comprehension is used to extract the first element of each tuple in the sorted_pairs list
    sorted_names = [pair[0] for pair in sorted_pairs]
    
    return sorted_names