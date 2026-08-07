# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def maxSubarrayWithEqualProducts(nums):
    # Initialize variables to store the maximum subarray sum and the current subarray sum
    max_sum = float('-inf')  
    current_sum = 1
    
    # Initialize variables to store the maximum product and the current product
    max_product = float('-inf')  
    current_product = 1
    
    # Initialize variables to store the start and end indices of the maximum subarray
    start = 0  
    end = 0
    
    # Initialize a variable to store the start index of the current subarray
    current_start = 0  
    
    # Iterate over the input array
    for i in range(len(nums)):
        # If the current element is 0, reset the current subarray sum and product
        if nums[i] == 0:
            current_sum = 1
            current_product = 1
            current_start = i + 1
        # If the current element is negative, update the current subarray sum and product
        elif nums[i] < 0:
            current_sum = -current_sum
            current_product *= nums[i]
        # If the current element is positive, update the current subarray sum and product
        else:
            current_sum += nums[i]
            current_product *= nums[i]
        
        # Update the maximum subarray sum and product if the current subarray sum is greater
        if current_sum > max_sum:
            max_sum = current_sum
            max_product = current_product
            start = current_start
            end = i
    
    # Return the maximum subarray with equal products
    return nums[start:end+1]