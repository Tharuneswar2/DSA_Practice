# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def generateTheString(n: int) -> str:
    # If n is odd, we can simply return a string of 'a' repeated n times
    if n % 2 != 0:
        # This is because 'a' appears an odd number of times in the resulting string
        return 'a' * n
    else:
        # If n is even, we need to ensure that the resulting string has characters with odd counts
        # We can achieve this by appending 'b' to the string of 'a' repeated n-1 times
        # This way, 'a' appears an odd number of times (n-1) and 'b' appears an odd number of times (1)
        return 'a' * (n-1) + 'b'