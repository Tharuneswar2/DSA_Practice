def minMoves2(nums):
    # First, sort the array
    nums.sort()
    
    # Calculate the median of the array
    median = nums[len(nums) // 2]
    
    # Initialize the total moves
    total_moves = 0
    
    # For each number in the array, calculate the absolute difference with the median
    # This difference represents the minimum number of moves required to make the number equal to the median
    for num in nums:
        total_moves += abs(num - median)
    
    # Return the total moves
    return total_moves