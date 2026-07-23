# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def smallestDivisible(n):
    # Initialize the result variable to 1, which is the smallest possible digit product
    result = 1
    
    # Loop through all numbers from 1 to n (inclusive) to find the smallest divisible digit product
    for i in range(1, n + 1):
        # If the current number is not divisible by the result, update the result
        if result % i != 0:
            # Calculate the least common multiple (LCM) of the result and the current number
            # This is done by multiplying the result with the current number and dividing by their greatest common divisor (GCD)
            result = result * i // gcd(result, i)
    
    # Return the smallest divisible digit product
    return result

# Function to calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm
def gcd(a, b):
    # If b is 0, the GCD is a
    if b == 0:
        return a
    # Otherwise, recursively call the GCD function with b and the remainder of a divided by b
    else:
        return gcd(b, a % b)