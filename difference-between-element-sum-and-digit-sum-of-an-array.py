# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def differenceBetweenElementSumAndDigitSum(arr):
    # Initialize two variables to store the sum of elements and the sum of digits
    element_sum = 0
    digit_sum = 0
    
    # Iterate over each element in the array
    for num in arr:
        # Add the current element to the element sum
        element_sum += num
        
        # Convert the current element to a string to easily iterate over its digits
        str_num = str(abs(num))  # abs is used to handle negative numbers
        
        # Iterate over each digit in the current element
        for digit in str_num:
            # Add the integer value of the current digit to the digit sum
            digit_sum += int(digit)
    
    # Return the absolute difference between the element sum and the digit sum
    return abs(element_sum - digit_sum)