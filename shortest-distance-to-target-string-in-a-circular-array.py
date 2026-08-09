# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def shortestDistanceToTarget(words, target, startIndex):
    # Initialize the result as infinity
    res = float('inf')
    
    # Calculate the total number of words
    n = len(words)
    
    # Traverse the array from startIndex to the end
    for i in range(startIndex, n + startIndex):
        # Check if the current word is the target
        if words[i % n] == target:
            # Update the result with the minimum distance
            res = min(res, min(i - startIndex, n - (i - startIndex)))
    
    # Return the result
    return res