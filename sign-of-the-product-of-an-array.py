# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def arraySign(nums):
    # Initialize a variable to store the sign of the product, assuming all numbers are positive
    sign = 1
    
    # Iterate over each number in the array
    for num in nums:
        # If the number is zero, the product will be zero, so return 0
        if num == 0:
            return 0
        # If the number is negative, flip the sign of the product
        elif num < 0:
            sign *= -1
    
    # Return the final sign of the product
    return sign