# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def runningSum(nums):
    # Initialize an empty list to store the running sum
    running_sum = []
    
    # Initialize a variable to keep track of the current sum
    current_sum = 0
    
    # Iterate over each number in the input list
    for num in nums:
        # Add the current number to the current sum
        current_sum += num
        
        # Append the current sum to the running sum list
        running_sum.append(current_sum)
    
    # Return the running sum list
    return running_sum