# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def countGoodNumbers(n: int) -> int:
    # Define the base values for even and odd numbers
    even_base = 20  # 2^10
    odd_base = 10   # 5^5
    
    # Calculate the number of even and odd numbers
    even_count = (n + 1) // 2
    odd_count = n // 2
    
    # Calculate the result using the properties of modular exponentiation
    result = pow(even_base, even_count, 10**9 + 7) * pow(odd_base, odd_count, 10**9 + 7)
    
    # Return the result modulo 10^9 + 7 to avoid overflow
    return result % (10**9 + 7)