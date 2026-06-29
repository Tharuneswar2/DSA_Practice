def sumOddLengthSubarrays(arr):
    n = len(arr)
    total_sum = 0
    
    # Iterate over all possible subarray lengths
    for length in range(1, n + 1):
        # Check if the length is odd
        if length % 2 != 0:
            # Iterate over all possible subarrays of the current length
            for i in range(n - length + 1):
                # Calculate the sum of the current subarray
                subarray_sum = sum(arr[i:i + length])
                # Add the sum of the current subarray to the total sum
                total_sum += subarray_sum
                
    return total_sum

def sumOddLengthSubarrays_optimized(arr):
    n = len(arr)
    total_sum = 0
    
    # Calculate the number of times each element appears in an odd length subarray
    for i in range(n):
        # The number of times the element appears is ((i + 1) * (n - i)) // 2
        # This is because the element can appear in ((i + 1) * (n - i)) subarrays
        # And half of these subarrays have an odd length
        count = ((i + 1) * (n - i) + 1) // 2
        # Add the contribution of the current element to the total sum
        total_sum += count * arr[i]
        
    return total_sum