# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def countTestedDevices(testOperations, devices):
    # Initialize a variable to store the total number of devices tested
    total_devices_tested = 0
    
    # Iterate over each test operation
    for operation in testOperations:
        # Extract the start and end indices of the operation
        start, end = operation
        
        # Calculate the number of devices tested in the current operation
        devices_tested = end - start + 1
        
        # Update the total number of devices tested
        total_devices_tested += devices_tested
        
        # Update the devices array to mark the devices as tested
        for i in range(start, end + 1):
            devices[i] = 1
    
    # Count the number of devices that were not tested
    devices_not_tested = devices.count(0)
    
    # Return the total number of devices tested
    return len(devices) - devices_not_tested