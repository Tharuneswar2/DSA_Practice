# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def findGCD(nums):
    # First, find the minimum number in the array, because GCD of an array cannot be greater than the smallest number
    min_num = min(nums)
    
    # Initialize the GCD with the smallest number
    gcd = min_num
    
    # Iterate from the smallest number down to 1
    for i in range(min_num, 0, -1):
        # Assume that the current number is the GCD
        is_gcd = True
        
        # Check if the current number is the divisor of all numbers in the array
        for num in nums:
            # If the current number is not the divisor of any number, break the loop
            if num % i != 0:
                is_gcd = False
                break
        
        # If the current number is the divisor of all numbers, it is the GCD
        if is_gcd:
            gcd = i
            break
    
    # Return the GCD
    return gcd