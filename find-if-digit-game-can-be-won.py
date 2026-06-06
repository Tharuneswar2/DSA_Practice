def canIWin(maxChoosableInteger, desiredTotal):
    if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
        return False

    memo = {}

    def can_win(choices, total):
        # Create a key for memoization
        key = tuple(choices)

        # If the result is already in memo, return it
        if key in memo:
            return memo[key]

        # If the current player can win, return True
        for i in range(len(choices)):
            if choices[i] >= total:
                memo[key] = True
                return True

        # Try all possible moves
        for i in range(len(choices)):
            # Skip the current choice if it's already used
            if choices[i] == 0:
                continue

            # Mark the current choice as used
            choices[i] = 0

            # If the next player can't win, the current player can win
            if not can_win(choices[:i] + choices[i+1:], total - choices[i]):
                memo[key] = True
                return True

            # Backtrack
            choices[i] = key[i]

        # If no winning move is found, return False
        memo[key] = False
        return False

    # Initialize the choices and start the game
    choices = list(range(1, maxChoosableInteger + 1))
    return can_win(choices, desiredTotal)