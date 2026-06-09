def flipLights(n, m):
    # If the number of flips is 0, all lights are on
    if m == 0:
        return 1
    
    # If the number of lights is 1, there are 2 possible states: on or off
    if n == 1:
        return 2
    
    # If the number of lights is 2, there are 4 possible states: on-on, on-off, off-on, off-off
    if n == 2:
        if m == 1:
            return 3
        else:
            return 4
    
    # If the number of lights is more than 2, we can consider the first two lights as a group
    # and the rest of the lights as another group
    # We can flip the first group in 4 ways (on-on, on-off, off-on, off-off)
    # and the rest of the group in 2 ways (all on or all off)
    # So, the total number of ways is 4 * 2 = 8
    # However, we need to subtract 2 because we counted the cases where all lights are on or off twice
    if m == 1:
        return 4
    elif m == 2:
        return 7
    else:
        return 8