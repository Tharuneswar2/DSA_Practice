def isThree(n: int) -> bool:
    # Initialize a counter for divisors
    count = 0
    
    # Iterate from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, increment the count
            count += 1
            
            # If the count exceeds 3, we can break the loop
            if count > 3:
                break
    
    # Return True if the count is exactly 3, False otherwise
    return count == 3