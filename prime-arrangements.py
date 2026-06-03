def numPrimeArrangements(n):
    def is_prime(num):
        # Check if a number is prime
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Count the number of primes less than or equal to n
    prime_count = sum(1 for i in range(2, n + 1) if is_prime(i))
    non_prime_count = n - prime_count

    # Calculate the number of arrangements
    import math
    prime_arrangements = math.factorial(prime_count)
    non_prime_arrangements = math.factorial(non_prime_count)
    total_arrangements = prime_arrangements * non_prime_arrangements

    return total_arrangements