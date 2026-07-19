# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def threeConsecutiveOdds(arr):
    # Initialize a counter to track the number of consecutive odd numbers
    consecutive_odds = 0
    
    # Iterate over the array
    for num in arr:
        # Check if the current number is odd
        if num % 2 != 0:
            # If the number is odd, increment the counter
            consecutive_odds += 1
            # If we have found three consecutive odd numbers, return True
            if consecutive_odds == 3:
                return True
        else:
            # If the number is even, reset the counter
            consecutive_odds = 0
    
    # If we have iterated over the entire array and haven't found three consecutive odd numbers, return False
    return False