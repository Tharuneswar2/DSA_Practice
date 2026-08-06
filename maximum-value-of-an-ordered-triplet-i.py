# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maximumProduct(nums):
    # Initialize minimum and maximum values with the first two elements of the array
    min1 = min2 = float('inf')  
    # Initialize maximum values with the first three elements of the array
    max1 = max2 = max3 = float('-inf')  

    # Iterate through the array to find the minimum and maximum values
    for n in nums:
        # Update minimum values
        if n <= min1:
            min1, min2 = n, min1
        elif n < min2:
            min2 = n

        # Update maximum values
        if n >= max1:
            max1, max2, max3 = n, max1, max2
        elif n >= max2:
            max2, max3 = n, max2
        elif n > max3:
            max3 = n

    # Return the maximum product of three numbers
    return max(min1 * min2 * max1, max1 * max2 * max3)