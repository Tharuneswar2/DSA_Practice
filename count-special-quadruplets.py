def countQuadruplets(nums):
    # Initialize count of quadruplets to 0
    count = 0
    
    # Iterate over all possible quadruplets
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                for last in range(k + 1, len(nums)):
                    # Check if the sum of the first three elements equals the fourth element
                    if nums[i] + nums[j] + nums[k] == nums[last]:
                        # If the condition is met, increment the count
                        count += 1
    
    # Return the total count of special quadruplets
    return count