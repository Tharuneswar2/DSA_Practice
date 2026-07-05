def is_prime(n):
    # Helper function to check if a number is prime
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def has_prime_frequency(nums):
    # Create a frequency dictionary
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Check if any frequency is prime
    for count in freq.values():
        if is_prime(count):
            return True
    
    return False

# Example usage
print(has_prime_frequency([1, 2, 2, 3, 3, 3]))  # True
print(has_prime_frequency([1, 1, 1, 2, 2, 2]))  # False