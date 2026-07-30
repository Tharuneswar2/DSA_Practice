# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def numberOfCuts(n: int) -> int:
    # If the number of cuts is 1 or less, we can't divide the circle into more than 1 piece
    if n < 2:
        return 0
    
    # If the number of cuts is 2, we can divide the circle into 2 pieces
    if n == 2:
        return 1
    
    # If the number of cuts is even, we can divide the circle into n//2 pieces
    if n % 2 == 0:
        # We need n//2 - 1 cuts to divide the circle into n//2 pieces
        return n // 2
    
    # If the number of cuts is odd, we can divide the circle into (n+1)//2 pieces
    else:
        # We need (n+1)//2 - 1 cuts to divide the circle into (n+1)//2 pieces
        return (n + 1) // 2