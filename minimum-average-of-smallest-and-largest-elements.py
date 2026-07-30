# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def minimumAverageDifference(nums):
    # Calculate the total sum of the array
    total_sum = sum(nums)
    
    # Initialize variables to keep track of the minimum difference and the index at which it occurs
    min_diff = float('inf')
    min_index = -1
    
    # Initialize a variable to keep track of the cumulative sum
    cumulative_sum = 0
    
    # Iterate over the array
    for i in range(len(nums)):
        # Add the current element to the cumulative sum
        cumulative_sum += nums[i]
        
        # Calculate the average of the smallest and largest elements
        avg = cumulative_sum // (i + 1)
        
        # If it's not the last element, calculate the average of the remaining elements
        if i != len(nums) - 1:
            avg2 = (total_sum - cumulative_sum) // (len(nums) - i - 1)
        else:
            avg2 = 0
        
        # Calculate the absolute difference between the two averages
        diff = abs(avg - avg2)
        
        # Update the minimum difference and index if the current difference is smaller
        if diff < min_diff:
            min_diff = diff
            min_index = i
    
    # Return the index at which the minimum difference occurs
    return min_index