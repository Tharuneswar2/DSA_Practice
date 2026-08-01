# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def numberOfArithmeticSlices(nums):
    # Initialize the count of arithmetic triplets
    count = 0
    
    # Iterate over the list of numbers
    for i in range(len(nums) - 2):
        # Initialize the difference between the first two numbers
        diff = nums[i + 1] - nums[i]
        
        # Iterate over the remaining numbers
        for j in range(i + 2, len(nums)):
            # If the difference between the current number and the previous number is the same as the initial difference
            if nums[j] - nums[j - 1] == diff:
                # Increment the count of arithmetic triplets
                count += 1
                
    # Return the count of arithmetic triplets
    return count