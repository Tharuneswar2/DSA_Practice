# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def canIWin(maxChoosableInteger, desiredTotal):
    # Create a bitmask to represent the state of the game
    # Each bit in the bitmask corresponds to a number from 1 to maxChoosableInteger
    # If the bit is 1, the number is available; if the bit is 0, the number is not available
    memo = {}
    
    def can_win(mask, total):
        # If the current state is already in the memo, return the result directly
        if mask in memo:
            return memo[mask]
        
        # Iterate over each number from 1 to maxChoosableInteger
        for i in range(1, maxChoosableInteger + 1):
            # Calculate the bitmask for the current number
            bit = 1 << (i - 1)
            
            # If the current number is available
            if mask & bit:
                # If the current number is greater than or equal to the remaining total, return True
                if i >= total:
                    memo[mask] = True
                    return True
                
                # Recursively check if the opponent can win
                # If the opponent cannot win, the current player can win
                if not can_win(mask ^ bit, total - i):
                    memo[mask] = True
                    return True
        
        # If no number can lead to a win, return False
        memo[mask] = False
        return False
    
    # Calculate the total sum of numbers from 1 to maxChoosableInteger
    total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
    
    # If the total sum is less than the desired total, return False
    if total_sum < desiredTotal:
        return False
    
    # If the total sum is equal to the desired total, return True if maxChoosableInteger is 1
    if total_sum == desiredTotal:
        return maxChoosableInteger == 1
    
    # Initialize the bitmask with all numbers available
    mask = (1 << maxChoosableInteger) - 1
    
    # Return the result of the recursive function
    return can_win(mask, desiredTotal)