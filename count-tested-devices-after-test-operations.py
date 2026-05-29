def count_tested_devices(test_operations):
    # Initialize a set to store unique devices
    tested_devices = set()
    
    # Iterate over each operation in the test operations
    for operation in test_operations:
        # If the operation is 1, add the device to the set
        if operation[0] == 1:
            tested_devices.add(operation[1])
        # If the operation is 2, remove the device from the set
        elif operation[0] == 2:
            tested_devices.discard(operation[1])
    
    # Return the number of unique devices tested
    return len(tested_devices)

# Example usage:
test_operations = [[1, 1], [1, 2], [2, 1], [1, 3]]
print(count_tested_devices(test_operations))  # Output: 2