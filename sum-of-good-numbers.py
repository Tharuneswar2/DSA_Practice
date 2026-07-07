def countGoodNumbers(n: int) -> int:
    MOD = 10**9 + 7
    # Calculate the number of even and odd positions
    even_count = n // 2
    odd_count = n - even_count
    
    # Calculate the number of 2s and 5s
    twos = pow(2, even_count, MOD)
    fives = pow(5, odd_count, MOD)
    
    # Calculate the number of good numbers
    good_numbers = (twos * fives) % MOD
    
    return good_numbers