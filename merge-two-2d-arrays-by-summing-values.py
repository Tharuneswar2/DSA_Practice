def merge_arrays(arr1, arr2):
    # Create a dictionary to store the sum of values for each key
    merged_dict = {}

    # Iterate over the first array
    for key, value in arr1:
        # Add the key-value pair to the dictionary
        merged_dict[key] = value

    # Iterate over the second array
    for key, value in arr2:
        # If the key already exists in the dictionary, add the value to it
        if key in merged_dict:
            merged_dict[key] += value
        # If the key does not exist, add it to the dictionary
        else:
            merged_dict[key] = value

    # Convert the dictionary back to a list of tuples
    merged_array = list(merged_dict.items())

    return merged_array

# Example usage:
arr1 = [(1, 10), (2, 20), (3, 30)]
arr2 = [(1, 5), (2, 10), (4, 40)]
print(merge_arrays(arr1, arr2))  # Output: [(1, 15), (2, 30), (3, 30), (4, 40)]