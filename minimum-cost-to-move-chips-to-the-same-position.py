# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minCostToMoveChips(position):
    # Initialize variables to store the count of chips at odd and even positions
    odd_count = 0
    even_count = 0
    
    # Iterate over each position
    for pos in position:
        # If the position is odd, increment the odd count
        if pos % 2 != 0:
            odd_count += 1
        # If the position is even, increment the even count
        else:
            even_count += 1
    
    # The minimum cost is the minimum of the count of chips at odd positions and the count of chips at even positions
    # This is because we can move all chips to either an odd or an even position with a cost equal to the count of chips at the other type of position
    return min(odd_count, even_count)