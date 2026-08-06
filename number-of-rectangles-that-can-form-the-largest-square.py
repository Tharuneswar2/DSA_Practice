# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countGoodRectangles(rectangles):
    # Initialize a hashmap to store the frequency of each square side length
    freq = {}
    
    # Initialize the maximum side length and its frequency
    max_side = 0
    max_freq = 0
    
    # Iterate over each rectangle
    for length, width in rectangles:
        # Calculate the side length of the square that can be formed
        side = min(length, width)
        
        # Update the frequency of the side length in the hashmap
        freq[side] = freq.get(side, 0) + 1
        
        # Update the maximum side length and its frequency
        if side > max_side:
            max_side = side
            max_freq = freq[side]
    
    # Return the frequency of the maximum side length
    return max_freq