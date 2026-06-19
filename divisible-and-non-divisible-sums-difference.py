def divisibleSumPairs(n, k, ar):
    # Initialize count of pairs where sum is divisible by k
    count = 0
    
    # Iterate over the array
    for i in range(n):
        # For each element, iterate over the rest of the array
        for j in range(i + 1, n):
            # Check if the sum of the pair is divisible by k
            if (ar[i] + ar[j]) % k == 0:
                # If it is, increment the count
                count += 1
                
    # Return the count
    return count

# Test the function
n = 6
k = 3
ar = [1, 2, 3, 4, 5, 6]
print(divisibleSumPairs(n, k, ar))