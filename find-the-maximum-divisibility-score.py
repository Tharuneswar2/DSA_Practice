# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def maxDivScore(nums, divisors):
    # Initialize a dictionary to store the frequency of each divisor
    freq = {}
    
    # Iterate over each divisor
    for divisor in divisors:
        # Initialize the count of numbers divisible by the current divisor to 0
        freq[divisor] = 0
        
        # Iterate over each number in the list
        for num in nums:
            # If the number is divisible by the current divisor, increment the count
            if num % divisor == 0:
                freq[divisor] += 1
                
    # Initialize the maximum score and the corresponding divisor
    max_score = 0
    max_divisor = None
    
    # Iterate over each divisor and its frequency
    for divisor, count in freq.items():
        # If the frequency of the current divisor is greater than the maximum score, update the maximum score and the corresponding divisor
        if count > max_score:
            max_score = count
            max_divisor = divisor
            
    # Return the divisor with the maximum score
    return max_divisor