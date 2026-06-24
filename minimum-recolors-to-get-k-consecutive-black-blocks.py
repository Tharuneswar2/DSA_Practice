def minimumRecolors(blocks, k):
    # Initialize the count of black blocks and the minimum recolors needed
    black_blocks = 0
    min_recolors = float('inf')
    
    # Initialize the left pointer of the sliding window
    left = 0
    
    # Traverse the blocks
    for right in range(len(blocks)):
        # If the current block is black, increment the count
        if blocks[right] == 'B':
            black_blocks += 1
        
        # If the window size is equal to k
        if right - left + 1 == k:
            # Update the minimum recolors needed
            min_recolors = min(min_recolors, k - black_blocks)
            
            # If the leftmost block is black, decrement the count
            if blocks[left] == 'B':
                black_blocks -= 1
            
            # Move the left pointer to the right
            left += 1
    
    # Return the minimum recolors needed
    return min_recolors