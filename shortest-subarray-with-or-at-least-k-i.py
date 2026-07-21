# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def shortestSubarray(nums, k):
    # Initialize the queue to store indices of prefix sums
    queue = []
    # Initialize the minimum length of subarray
    min_length = float('inf')
    # Initialize the prefix sum
    prefix_sum = 0
    
    # Iterate over the array
    for i, num in enumerate(nums):
        # Update the prefix sum
        prefix_sum ^= num
        
        # If the prefix sum is greater than or equal to k, update the minimum length
        if prefix_sum >= k:
            min_length = min(min_length, i + 1)
        
        # While the queue is not empty and the prefix sum is less than the prefix sum at the front of the queue
        while queue and prefix_sum < queue[0][0]:
            # Remove the front element from the queue
            queue.pop(0)
        
        # If the queue is not empty and the prefix sum is greater than or equal to the prefix sum at the back of the queue
        if queue and prefix_sum >= queue[-1][0]:
            # Update the minimum length
            min_length = min(min_length, i - queue[-1][1])
        
        # Add the prefix sum and its index to the queue
        queue.append((prefix_sum, i))
    
    # Return the minimum length if it's not infinity, otherwise return -1
    return min_length if min_length != float('inf') else -1