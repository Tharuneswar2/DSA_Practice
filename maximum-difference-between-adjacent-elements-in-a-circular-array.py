# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maximumGap(nums):
    # Check if the input list is empty or contains less than 2 elements
    if len(nums) < 2:
        return 0
    
    # Find the minimum and maximum values in the list
    min_val = min(nums)
    max_val = max(nums)
    
    # If all elements are the same, return 0
    if min_val == max_val:
        return 0
    
    # Calculate the bucket size
    bucket_size = max(1, (max_val - min_val) // (len(nums) - 1))
    
    # Initialize the bucket list with default values
    bucket = [[float('inf'), float('-inf')] for _ in range((max_val - min_val) // bucket_size + 1)]
    
    # Distribute the elements into the buckets
    for num in nums:
        index = (num - min_val) // bucket_size
        bucket[index][0] = min(bucket[index][0], num)
        bucket[index][1] = max(bucket[index][1], num)
    
    # Initialize the maximum gap and the previous maximum value
    max_gap = 0
    prev_max = bucket[0][1]
    
    # Iterate over the buckets to find the maximum gap
    for i in range(1, len(bucket)):
        if bucket[i][0] != float('inf'):
            max_gap = max(max_gap, bucket[i][0] - prev_max)
            prev_max = bucket[i][1]
    
    # Consider the gap between the last bucket and the first bucket
    max_gap = max(max_gap, bucket[0][0] - prev_max, bucket[0][1] - prev_max)
    
    return max_gap