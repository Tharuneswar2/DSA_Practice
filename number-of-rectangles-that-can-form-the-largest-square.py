def countGoodRectangles(rectangles):
    # Create a dictionary to store the frequency of each square side length
    freq = {}
    
    # Initialize the maximum side length and its frequency
    max_side = 0
    max_freq = 0
    
    # Iterate over each rectangle
    for length, width in rectangles:
        # Calculate the side length of the square that can be formed
        side = min(length, width)
        
        # Update the frequency of the side length
        freq[side] = freq.get(side, 0) + 1
        
        # Update the maximum side length and its frequency
        if side > max_side:
            max_side = side
            max_freq = freq[side]
        elif side == max_side:
            max_freq += freq[side]
    
    # Return the frequency of the maximum side length
    return max_freq

# Example usage:
rectangles = [[5,8],[3,9],[5,12],[16,5]]
print(countGoodRectangles(rectangles))