def findChild(n, k):
    # Create a circular linked list with n children
    children = [i for i in range(1, n + 1)]
    
    # Initialize the index of the child who has the ball
    index = 0
    
    # Simulate the passing of the ball k times
    for _ in range(k):
        # The ball is passed to the next child
        index = (index + 1) % n
    
    # Return the child who has the ball after k seconds
    return children[index]

def findChildMath(n, k):
    # The child who has the ball after k seconds is the one at index (k - 1) % n
    # This is because the ball is passed to the next child k times, and the index wraps around to 0 when it reaches n
    return (k - 1) % n + 1

# Test the functions
n = 5  # number of children
k = 3  # number of seconds
print(findChild(n, k))  # Output: 3
print(findChildMath(n, k))  # Output: 3