def finalArrayStateAfterKMultiplicationOperations(arr, k):
    # Initialize an empty list to store the final array state
    final_state = []
    
    # Iterate over the array
    for num in arr:
        # If the number is not already in the final state, add it
        if num not in final_state:
            final_state.append(num)
    
    # Sort the final state in ascending order
    final_state.sort()
    
    # Return the final state
    return final_state

# Test the function
arr = [1, 2, 3, 2, 1]
k = 2
print(finalArrayStateAfterKMultiplicationOperations(arr, k))