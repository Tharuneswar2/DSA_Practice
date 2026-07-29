# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def sumBase(self, n: int, k: int) -> int:
    # Initialize sum variable to store the sum of digits in base k
    total_sum = 0
    
    # Continue the process until n becomes 0
    while n > 0:
        # Calculate the remainder of n when divided by k, this will give the last digit in base k
        remainder = n % k
        
        # Add the remainder to the total sum
        total_sum += remainder
        
        # Update n by performing integer division of n by k, effectively removing the last digit
        n = n // k
    
    # Return the total sum of digits in base k
    return total_sum