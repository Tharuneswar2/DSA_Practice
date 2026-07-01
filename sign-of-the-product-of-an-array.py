def arraySign(nums):
    # Initialize a variable to store the sign of the product
    sign = 1
    
    # Iterate over each number in the array
    for num in nums:
        # If the number is zero, the product will be zero, so return 0
        if num == 0:
            return 0
        # If the number is negative, flip the sign
        elif num < 0:
            sign *= -1
    
    # Return the final sign
    return sign