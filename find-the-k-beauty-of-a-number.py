# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def divisorGame(n: int) -> bool:
    # The key insight here is that the person who starts the game can always win if n is even
    # This is because they can choose to divide n by 2, forcing the other player to play with an odd number
    # The player who plays with an odd number will always lose, because no matter what divisor they choose, the result will be even
    # So, the first player can always win by mirroring the moves of the second player
    # Therefore, we can simply return whether n is even
    return n % 2 == 0