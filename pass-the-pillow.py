def pass_the_pillow(n, k):
    # Calculate the position of the pillow after k passes
    # We use the modulo operator to handle cases where k is greater than n
    position = (k - 1) % n + 1
    
    # Return the position of the pillow
    return position

# Test the function
n = int(input())
k = int(input())
print(pass_the_pillow(n, k))