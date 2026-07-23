# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def isThree(n: int) -> bool:
    # Initialize a counter to store the number of divisors
    count = 0
    
    # Iterate over all numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Check if 'i' is a divisor of 'n'
        if n % i == 0:
            # If 'i' is a divisor, increment the counter
            count += 1
            
            # If the number of divisors exceeds 3, we can break the loop
            if count > 3:
                break
                
    # Return True if the number of divisors is exactly 3, False otherwise
    return count == 3