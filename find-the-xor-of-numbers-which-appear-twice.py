def findSingle(nums):
    # Initialize result variable to 0. This variable will hold the XOR of all numbers in the array.
    result = 0
    
    # Iterate over each number in the array.
    for num in nums:
        # XOR the current number with the result. This works because XOR of a number with itself is 0, 
        # and XOR of a number with 0 is the number itself. So, all numbers that appear twice will be cancelled out.
        result ^= num
    
    # Return the result, which is the XOR of the number that appears only once.
    return result

# Test the function
nums = [2, 3, 5, 4, 5, 2, 4]
print(findSingle(nums))  # Output: 3