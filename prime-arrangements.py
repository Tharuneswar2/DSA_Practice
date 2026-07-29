# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def numPrimeArrangements(n):
    # Create a boolean array, prime, of size n+1
    prime = [True] * (n + 1)
    # 0 and 1 are not prime numbers
    prime[0] = prime[1] = False
    
    # Iterate from 2 to sqrt(n)
    for p in range(2, int(n ** 0.5) + 1):
        # If p is a prime, mark as composite all the multiples of p
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
                
    # Count the number of prime numbers
    count = sum(prime)
    
    # Calculate the number of arrangements of prime numbers
    prime_arrangements = 1
    for i in range(1, count + 1):
        prime_arrangements = (prime_arrangements * i) % (10 ** 9 + 7)
        
    # Calculate the number of arrangements of non-prime numbers
    non_prime_arrangements = 1
    for i in range(1, n - count + 1):
        non_prime_arrangements = (non_prime_arrangements * i) % (10 ** 9 + 7)
        
    # Return the total number of arrangements
    return (prime_arrangements * non_prime_arrangements) % (10 ** 9 + 7)