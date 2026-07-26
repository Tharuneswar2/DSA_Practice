# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minStartValue(nums):
    # Initialize the minimum sum and the current sum to the first element of the array
    min_sum = current_sum = nums[0]
    
    # Iterate over the array starting from the second element
    for num in nums[1:]:
        # Update the current sum by adding the current number
        current_sum += num
        
        # Update the minimum sum if the current sum is less than the minimum sum
        min_sum = min(min_sum, current_sum)
    
    # If the minimum sum is positive, return 1 because we can start with 1 and still get a positive step by step sum
    if min_sum >= 0:
        return 1
    # Otherwise, return the absolute value of the minimum sum plus 1
    else:
        return abs(min_sum) + 1