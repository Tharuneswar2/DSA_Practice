def maxProduct(nums):
    # Sort the array in ascending order
    nums.sort()
    
    # Calculate the product of the two largest numbers
    product1 = nums[-1] * nums[-2]
    
    # Calculate the product of the two smallest numbers (in case they are negative)
    product2 = nums[0] * nums[1]
    
    # Return the maximum product
    return max(product1, product2)

# Test the function
print(maxProduct([1, 20, 3, -10, 5]))  # Output: 200
print(maxProduct([-10, -10, 1, 3, 2]))  # Output: 100