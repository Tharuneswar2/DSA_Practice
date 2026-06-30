def difference_sum(arr):
    # Calculate the sum of elements in the array
    element_sum = sum(arr)
    
    # Initialize a variable to store the sum of digits
    digit_sum = 0
    
    # Iterate over each element in the array
    for num in arr:
        # Convert the number to a string to calculate the sum of its digits
        str_num = str(num)
        
        # Calculate the sum of digits of the current number
        for digit in str_num:
            digit_sum += int(digit)
    
    # Return the difference between the sum of elements and the sum of digits
    return element_sum - digit_sum

# Example usage:
arr = [1, 15, 6, 3]
print(difference_sum(arr))