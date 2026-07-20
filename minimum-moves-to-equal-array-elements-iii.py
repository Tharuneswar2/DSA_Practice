# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minMoves2(nums):
    # First, we sort the array in ascending order
    nums.sort()
    
    # We find the median of the array, which will be the target value that all elements will be equal to
    median = nums[len(nums) // 2]
    
    # Initialize a variable to store the total number of moves
    total_moves = 0
    
    # Iterate over each number in the array
    for num in nums:
        # For each number, the number of moves required to make it equal to the median is the absolute difference between the number and the median
        total_moves += abs(num - median)
    
    # Return the total number of moves
    return total_moves