def distinctAverages(nums):
    # Create a set to store unique averages
    averages = set()
    
    # Iterate over all possible pairs of numbers in the list
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Calculate the average of the current pair
            avg = (nums[i] + nums[j]) / 2
            
            # Add the average to the set
            averages.add(avg)
    
    # Return the number of unique averages
    return len(averages)