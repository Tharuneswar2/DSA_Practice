def runningSum(nums):
    # Initialize the running sum to 0
    running_sum = 0
    
    # Initialize an empty list to store the running sums
    result = []
    
    # Iterate over each number in the input list
    for num in nums:
        # Add the current number to the running sum
        running_sum += num
        
        # Append the current running sum to the result list
        result.append(running_sum)
    
    # Return the list of running sums
    return result

# Alternatively, you can use a list comprehension with the accumulate function from the itertools module
from itertools import accumulate

def runningSum(nums):
    # Use the accumulate function to calculate the running sum
    # and convert the result to a list
    return list(accumulate(nums))