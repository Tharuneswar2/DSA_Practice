# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maxAscendingSum(nums):
    # Initialize variables to store the maximum sum and the current sum
    max_sum = float('-inf')  # Initialize max_sum as negative infinity
    current_sum = nums[0]  # Initialize current_sum with the first element of the array
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is greater than the previous element, add it to the current sum
        if nums[i] > nums[i - 1]:
            current_sum += nums[i]
        # If the current element is not greater than the previous element, update max_sum if necessary and reset current_sum
        else:
            max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is greater
            current_sum = nums[i]  # Reset current_sum with the current element
    
    # Update max_sum one last time after the loop ends
    max_sum = max(max_sum, current_sum)
    
    return max_sum