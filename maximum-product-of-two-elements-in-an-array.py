# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maxProduct(nums):
    # Check if the input list has less than 2 elements
    if len(nums) < 2:
        return None
    
    # Initialize max1 and max2 as negative infinity
    # These variables will store the maximum and second maximum numbers in the array
    max1, max2 = float('-inf'), float('-inf')
    
    # Iterate through the array to find the maximum and second maximum numbers
    for num in nums:
        # If the current number is greater than max1, update max1 and max2
        if num > max1:
            max2 = max1
            max1 = num
        # If the current number is less than max1 but greater than max2, update max2
        elif num > max2:
            max2 = num
    
    # Return the product of max1 and max2
    return max1 * max2