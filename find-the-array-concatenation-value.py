def findConcatenatedValue(arr):
    # Initialize an empty list to store concatenated values
    concatenated_values = []
    
    # Iterate over each element in the array
    for i in range(len(arr)):
        # Concatenate the current element with the next element
        # Use modulo to wrap around to the start of the array for the last element
        concatenated_value = int(str(arr[i]) + str(arr[(i + 1) % len(arr)]))
        
        # Append the concatenated value to the list
        concatenated_values.append(concatenated_value)
    
    # Return the minimum concatenated value
    return min(concatenated_values)

# Example usage:
arr = [1, 2, 3, 4]
print(findConcatenatedValue(arr))