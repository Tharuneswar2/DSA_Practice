def mergeSimilarItems(items1, items2):
    # Combine the two lists of items
    items = items1 + items2
    
    # Create a dictionary to store the items and their values
    item_dict = {}
    
    # Iterate over each item in the combined list
    for item, value in items:
        # If the item is already in the dictionary, add the value to it
        if item in item_dict:
            item_dict[item] += value
        # If the item is not in the dictionary, add it with its value
        else:
            item_dict[item] = value
    
    # Sort the items by their values in descending order
    sorted_items = sorted(item_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Return the sorted list of items
    return sorted_items

# Example usage:
items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
print(mergeSimilarItems(items1, items2))