def maxProductDifference(nums):
    # Sort the list in ascending order
    nums.sort()
    
    # The maximum product difference will be between the product of the last two elements 
    # and the product of the first two elements
    max_product = nums[-1] * nums[-2]
    min_product = nums[0] * nums[1]
    
    # Return the difference between the maximum product and the minimum product
    return max_product - min_product

# Test the function
print(maxProductDifference([5, 6, 2, 7, 4]))