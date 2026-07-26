# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countQuadruplets(nums):
    # Initialize count variable to store the total number of special quadruplets
    count = 0
    
    # Iterate over the array with four nested loops to generate all possible quadruplets
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                for last in range(k + 1, len(nums)):
                    # Check if the sum of the first two elements is equal to the sum of the last two elements
                    if nums[i] + nums[j] == nums[k] + nums[last]:
                        # If the condition is met, increment the count
                        count += 1
    
    # Return the total count of special quadruplets
    return count