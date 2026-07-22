# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def findChild(n, k):
    # Initialize the child who has the ball as 1 (since we start with child 1)
    child_with_ball = 1
    
    # Iterate from 2 to n (since we have n children)
    for i in range(2, n + 1):
        # Update the child who has the ball using the recursive formula: (child_with_ball + k) % i
        # The modulus operation ensures the child index wraps around to the start if it exceeds the current number of children
        child_with_ball = (child_with_ball + k) % i
        
        # If the result of the modulus operation is 0, it means the ball is with the last child, so we update it to i
        if child_with_ball == 0:
            child_with_ball = i
    
    # Return the child who has the ball after k seconds
    return child_with_ball