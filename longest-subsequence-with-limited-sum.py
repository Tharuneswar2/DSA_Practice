def longestSubsequence(nums, k):
    # Sort the array in ascending order
    nums.sort()
    
    # Initialize variables to store the result and the current sum
    res = []
    curr_sum = 0
    
    # Iterate over the sorted array
    for num in nums:
        # If adding the current number to the sum does not exceed k, add it to the result and update the sum
        if curr_sum + num <= k:
            res.append(num)
            curr_sum += num
        # If adding the current number exceeds k, break the loop
        else:
            break
    
    return res

def longestSubsequenceWithLimitedSum(nums, k):
    # Initialize variables to store the result and the maximum length
    res = []
    max_len = 0
    
    # Iterate over all possible subsequences
    for i in range(1 << len(nums)):
        subsequence = [nums[j] for j in range(len(nums)) if (i & (1 << j))]
        
        # Calculate the sum of the current subsequence
        subsequence_sum = sum(subsequence)
        
        # If the sum of the current subsequence does not exceed k and its length is greater than the maximum length, update the result and the maximum length
        if subsequence_sum <= k and len(subsequence) > max_len:
            res = subsequence
            max_len = len(subsequence)
    
    return res