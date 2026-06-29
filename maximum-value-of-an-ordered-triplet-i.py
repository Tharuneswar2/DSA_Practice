def maximumProduct(nums):
    # Initialize the minimum and maximum values with the first three elements of the array
    min1, min2 = float('inf'), float('inf')
    max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')

    # Iterate through the array to find the minimum and maximum values
    for num in nums:
        # Update the minimum values
        if num <= min1:
            min1, min2 = num, min1
        elif num < min2:
            min2 = num

        # Update the maximum values
        if num >= max1:
            max1, max2, max3 = num, max1, max2
        elif num >= max2:
            max2, max3 = num, max2
        elif num > max3:
            max3 = num

    # Return the maximum product
    return max(min1 * min2 * max1, max1 * max2 * max3)