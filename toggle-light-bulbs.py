# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def flipLights(n, m):
    # If the number of operations is 0, return the initial state of the light bulbs
    if m == 0:
        return 1
    
    # If the number of light bulbs is 1, there are only 2 possible states: on or off
    if n == 1:
        return 2
    
    # If the number of light bulbs is 2, there are 4 possible states: on-on, on-off, off-on, off-off
    if n == 2:
        # If the number of operations is 1, there are 3 possible states: on-on, on-off, off-on
        if m == 1:
            return 3
        # If the number of operations is 2 or more, there are 4 possible states: on-on, on-off, off-on, off-off
        else:
            return 4
    
    # If the number of light bulbs is 3 or more, there are 8 possible states: on-on-on, on-on-off, on-off-on, on-off-off, off-on-on, off-on-off, off-off-on, off-off-off
    # If the number of operations is 1, there are 4 possible states: on-on-on, on-on-off, off-on-on, off-off-off
    if m == 1:
        return 4
    # If the number of operations is 2, there are 7 possible states: on-on-on, on-on-off, on-off-on, on-off-off, off-on-on, off-on-off, off-off-off
    elif m == 2:
        return 7
    # If the number of operations is 3 or more, there are 8 possible states: on-on-on, on-on-off, on-off-on, on-off-off, off-on-on, off-on-off, off-off-on, off-off-off
    else:
        return 8