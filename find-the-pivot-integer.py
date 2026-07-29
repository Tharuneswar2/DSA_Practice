# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def find_pivot(n):
    # Calculate the sum of all numbers from 1 to n using Gauss' formula
    total_sum = n * (n + 1) // 2
    
    # Initialize the left sum to 0
    left_sum = 0
    
    # Iterate over all numbers from 1 to n
    for i in range(1, n + 1):
        # If the left sum is equal to the total sum minus the left sum and the current number
        if left_sum == total_sum - left_sum - i:
            # Return the current number as it is the pivot integer
            return i
        # Otherwise, add the current number to the left sum
        left_sum += i
    
    # If no pivot integer is found, return -1
    return -1