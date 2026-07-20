# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def minBitwiseORArray(nums):
    # Initialize an empty list to store the result
    res = []
    
    # Iterate over the input list
    for num in nums:
        # If the result list is empty or the current number is less than the last number in the result list, 
        # append the current number to the result list
        if not res or num < res[-1]:
            res.append(num)
        else:
            # Initialize a variable to store the bitwise OR of the current number and the last number in the result list
            bitwise_or = res[-1] | num
            
            # If the bitwise OR is equal to the last number in the result list, 
            # it means the current number does not change the result, so we skip it
            if bitwise_or == res[-1]:
                continue
            else:
                # Otherwise, append the bitwise OR to the result list
                res.append(bitwise_or)
    
    # Return the result list
    return res