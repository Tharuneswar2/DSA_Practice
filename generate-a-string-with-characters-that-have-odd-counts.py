def generateTheString(n: int) -> str:
    # If n is odd, we can simply return a string of 'a' repeated n times
    if n % 2 != 0:
        return 'a' * n
    
    # If n is even, we need to return a string with one 'a' and the rest 'b's
    # This way, 'a' has an odd count (1) and 'b' has an even count (n-1)
    else:
        return 'a' + 'b' * (n - 1)