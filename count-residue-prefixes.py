def countPrefixes(arr, n, x):
    # Initialize count of prefixes with non-zero residues
    count = 0
    
    # Initialize prefix sum
    prefix_sum = 0
    
    # Iterate over the array
    for i in range(n):
        # Add current element to prefix sum
        prefix_sum += arr[i]
        
        # If prefix sum is not divisible by x, increment count
        if prefix_sum % x != 0:
            count += 1
    
    # Return count of prefixes with non-zero residues
    return count

# Test the function
arr = [1, 2, 3, 4, 5]
n = len(arr)
x = 3
print(countPrefixes(arr, n, x))