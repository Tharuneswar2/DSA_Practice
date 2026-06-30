def maxDivScore(nums, divisors):
    # Initialize the maximum score and the corresponding divisor
    max_score = 0
    max_divisor = 0
    
    # Iterate over each divisor
    for divisor in divisors:
        # Initialize the score for the current divisor
        score = 0
        
        # Iterate over each number in the list
        for num in nums:
            # If the number is divisible by the divisor, increment the score
            if num % divisor == 0:
                score += 1
        
        # If the score for the current divisor is greater than the max score, update the max score and divisor
        if score > max_score:
            max_score = score
            max_divisor = divisor
    
    # Return the divisor with the maximum score
    return max_divisor

# Example usage:
nums = [4, 8, 15, 16]
divisors = [2, 3, 5, 6, 7]
print(maxDivScore(nums, divisors))