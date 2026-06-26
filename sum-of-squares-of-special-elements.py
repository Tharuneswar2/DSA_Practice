def sum_of_squares_of_special_elements(arr):
    # Initialize sum of squares
    sum_of_squares = 0
    
    # Iterate over each element in the array
    for i in range(len(arr)):
        # Check if the element is special (i.e., it is equal to its index)
        if arr[i] == i:
            # If the element is special, add its square to the sum
            sum_of_squares += arr[i] ** 2
    
    # Return the sum of squares of special elements
    return sum_of_squares

# Example usage:
arr = [0, 1, 2, 3, 4]
print(sum_of_squares_of_special_elements(arr))