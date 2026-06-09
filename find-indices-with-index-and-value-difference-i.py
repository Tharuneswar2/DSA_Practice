def fairCandySwap(A, B):
    # Calculate the difference in total candies between Alice and Bob
    diff = (sum(A) - sum(B)) // 2
    
    # Create a set of Bob's candies for efficient lookups
    B_set = set(B)
    
    # Iterate over Alice's candies
    for candy in A:
        # Check if swapping the current candy with a candy from Bob would result in equal total candies
        if candy - diff in B_set:
            return [candy, candy - diff]