# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minSubsequence(nums):
    # Sort the list in descending order to prioritize larger numbers
    nums.sort(reverse=True)
    
    # Initialize variables to store the total sum of the original list and the sum of the subsequence
    total_sum = sum(nums)
    subsequence_sum = 0
    
    # Initialize an empty list to store the subsequence
    subsequence = []
    
    # Iterate over the sorted list
    for num in nums:
        # Add the current number to the subsequence
        subsequence.append(num)
        
        # Add the current number to the subsequence sum
        subsequence_sum += num
        
        # If the subsequence sum is greater than half of the total sum, break the loop
        if subsequence_sum > total_sum / 2:
            break
    
    # Return the subsequence
    return subsequence