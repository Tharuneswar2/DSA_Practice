def numberOfChangingKeys(keys, values):
    # Initialize a dictionary to store the keys and their corresponding values
    key_values = {}
    
    # Initialize a variable to store the count of changing keys
    changing_keys = 0
    
    # Iterate over the keys and values
    for key, value in zip(keys, values):
        # If the key is already in the dictionary and its value is different
        if key in key_values and key_values[key] != value:
            # Increment the count of changing keys
            changing_keys += 1
        # Update the value of the key in the dictionary
        key_values[key] = value
    
    # Return the count of changing keys
    return changing_keys

# Test the function
keys = [1, 2, 3, 1, 2, 3]
values = [10, 20, 30, 40, 50, 60]
print(numberOfChangingKeys(keys, values))  # Output: 3