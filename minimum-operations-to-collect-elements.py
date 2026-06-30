def min_operations_to_collect_elements(arr):
    # Initialize variables to store the minimum operations and the current sum
    min_operations = float('inf')
    current_sum = 0
    
    # Iterate over the array to calculate the prefix sum
    prefix_sum = [0] * len(arr)
    for i in range(len(arr)):
        # Calculate the prefix sum at each index
        prefix_sum[i] = arr[i] + (prefix_sum[i-1] if i > 0 else 0)
    
    # Iterate over the array to calculate the minimum operations
    for i in range(len(arr)):
        # Calculate the sum of elements from the current index to the end
        current_sum = prefix_sum[-1] - (prefix_sum[i-1] if i > 0 else 0)
        
        # Calculate the operations required to collect elements from the current index to the end
        operations = current_sum // arr[i]
        
        # Update the minimum operations if the current operations are less
        min_operations = min(min_operations, operations)
    
    return min_operations

# Example usage
arr = [2, 3, 5, 7, 11]
print(min_operations_to_collect_elements(arr))