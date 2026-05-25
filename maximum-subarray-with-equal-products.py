def maxSubarray(nums):
    # Initialize variables to store the maximum subarray sum and the current subarray sum
    max_sum = float('-inf')
    current_sum = 1
    
    # Initialize variables to store the maximum subarray product and the current subarray product
    max_product = float('-inf')
    current_product = 1
    
    # Initialize variables to store the start and end indices of the maximum subarray
    start = 0
    end = 0
    
    # Initialize variables to store the start and end indices of the current subarray
    temp_start = 0
    
    # Iterate over the array
    for i in range(len(nums)):
        # If the current element is 0, reset the current subarray sum and product
        if nums[i] == 0:
            current_sum = 1
            current_product = 1
            temp_start = i + 1
        # If the current element is negative, update the current subarray sum and product
        elif nums[i] < 0:
            current_sum = -current_sum
            current_product *= nums[i]
        # If the current element is positive, update the current subarray sum and product
        else:
            current_sum += nums[i]
            current_product *= nums[i]
        
        # Update the maximum subarray sum and product if the current subarray sum and product are greater
        if current_sum > max_sum:
            max_sum = current_sum
            max_product = current_product
            start = temp_start
            end = i
    
    # Return the maximum subarray with equal products
    return nums[start:end+1]

def maxSubarrayWithEqualProducts(nums):
    # Initialize variables to store the maximum subarray sum and the current subarray sum
    max_sum = float('-inf')
    current_sum = 1
    
    # Initialize variables to store the maximum subarray product and the current subarray product
    max_product = float('-inf')
    current_product = 1
    
    # Initialize variables to store the start and end indices of the maximum subarray
    start = 0
    end = 0
    
    # Initialize variables to store the start and end indices of the current subarray
    temp_start = 0
    
    # Initialize a dictionary to store the products of subarrays
    products = {1: [0]}
    
    # Iterate over the array
    for i in range(len(nums)):
        # If the current element is 0, reset the current subarray sum and product
        if nums[i] == 0:
            current_sum = 1
            current_product = 1
            temp_start = i + 1
            products = {1: [i+1]}
        # If the current element is negative, update the current subarray sum and product
        elif nums[i] < 0:
            current_sum = -current_sum
            current_product *= nums[i]
            if current_product not in products:
                products[current_product] = [temp_start, i]
            else:
                products[current_product].append(i)
        # If the current element is positive, update the current subarray sum and product
        else:
            current_sum += nums[i]
            current_product *= nums[i]
            if current_product not in products:
                products[current_product] = [temp_start, i]
            else:
                products[current_product].append(i)
        
        # Update the maximum subarray sum and product if the current subarray sum and product are greater
        if current_sum > max_sum:
            max_sum = current_sum
            max_product = current_product
            start = temp_start
            end = i
    
    # Find the maximum subarray with equal products
    max_length = 0
    max_subarray = []
    for product, indices in products.items():
        for i in range(len(indices) - 1):
            if indices[i+1] - indices[i] > max_length:
                max_length = indices[i+1] - indices[i]
                max_subarray = nums[indices[i]:indices[i+1]]
    
    # Return the maximum subarray with equal products
    return max_subarray