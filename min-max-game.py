# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def minMaxGame(nums):
    # Base case: if the length of the array is 1, return the only element
    if len(nums) == 1:
        return nums[0]
    
    # Initialize the result array with the same length as the input array
    res = [0] * (len(nums) // 2)
    
    # Iterate over the input array in steps of 2
    for i in range(len(nums) // 2):
        # For each pair of elements, calculate the minimum and maximum
        # and store the minimum of the maximum and the maximum of the minimum in the result array
        res[i] = min(max(nums[2*i], nums[2*i+1]), max(min(nums[2*i], nums[2*i+1]), min(nums[2*i+1], nums[2*i])))
    
    # Recursively call the function with the result array
    return minMaxGame(res)