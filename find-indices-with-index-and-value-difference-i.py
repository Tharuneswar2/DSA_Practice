# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def fairCandySwap(A, B):
    # Calculate the difference in total candies between Alice and Bob
    diff = (sum(A) - sum(B)) // 2
    
    # Create a set of Bob's candies for efficient lookups
    set_B = set(B)
    
    # Iterate over Alice's candies
    for candy in A:
        # Check if the candy that would make the difference zero is in Bob's set
        if candy - diff in set_B:
            # Return the pair of candies that would make the difference zero
            return [candy, candy - diff]