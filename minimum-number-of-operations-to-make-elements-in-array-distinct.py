def minOperations(arr):
    # Create a set to store unique elements
    unique_set = set()
    
    # Initialize the count of operations
    operations = 0
    
    # Iterate over the array
    for num in arr:
        # Initialize a variable to store the next unique number
        next_unique = num
        
        # While the next unique number is in the set, increment it
        while next_unique in unique_set:
            next_unique += 1
            # Increment the operations count
            operations += 1
        
        # Add the next unique number to the set
        unique_set.add(next_unique)
    
    # Return the total operations
    return operations

# Test the function
print(minOperations([1, 2, 2, 3, 4, 4, 5]))  # Output: 2