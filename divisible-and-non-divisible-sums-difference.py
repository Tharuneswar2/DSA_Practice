# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def divisibleSumPairs(n, k, ar):
    # Initialize a list to store the frequency of each remainder when divided by k
    remainder_freq = [0] * k
    
    # Iterate over each number in the array
    for num in ar:
        # Calculate the remainder when the number is divided by k
        remainder = num % k
        
        # Increment the frequency of the calculated remainder
        remainder_freq[remainder] += 1
    
    # Initialize the count of pairs with sum divisible by k
    count = 0
    
    # Calculate the count of pairs with sum divisible by k
    # For each remainder, calculate the number of pairs that can be formed with the same remainder
    # and add it to the count
    for i in range(1, (k + 1) // 2):
        # The number of pairs that can be formed with the same remainder is the product of the frequency of the remainder
        # and the frequency of the remainder that sums up to k
        count += remainder_freq[i] * remainder_freq[k - i]
    
    # If k is even, we need to consider the pairs with remainder k/2 separately
    if k % 2 == 0:
        # The number of pairs that can be formed with the remainder k/2 is the combination of 2 from the frequency of the remainder
        count += remainder_freq[k // 2] * (remainder_freq[k // 2] - 1) // 2
    
    # The number of pairs with sum not divisible by k is the total number of pairs minus the count of pairs with sum divisible by k
    non_divisible_pairs = n * (n - 1) // 2 - count
    
    # Return the absolute difference between the count of pairs with sum divisible by k and the count of pairs with sum not divisible by k
    return abs(count - non_divisible_pairs)