# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def findMaxK(nums):
    # Create a set to store the numbers we have seen so far for efficient lookups
    num_set = set()
    
    # Initialize the maximum positive integer that exists with its negative
    max_k = float('-inf')
    
    # Iterate over the list of numbers
    for num in nums:
        # If the negative of the current number exists in the set, update max_k
        if -num in num_set:
            max_k = max(max_k, num)
        # Add the current number to the set
        num_set.add(num)