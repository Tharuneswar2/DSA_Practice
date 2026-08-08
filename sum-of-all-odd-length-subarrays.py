# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def sumOddLengthSubarrays(arr):
    n = len(arr)  # get the length of the input array
    total_sum = 0  # initialize a variable to store the total sum
    
    # iterate over all possible subarray lengths (only odd lengths)
    for length in range(1, n + 1, 2):  
        # iterate over all possible subarrays of the current length
        for i in range(n - length + 1):  
            # calculate the sum of the current subarray
            subarray_sum = sum(arr[i:i + length])  
            # add the sum of the current subarray to the total sum
            total_sum += subarray_sum  
    
    return total_sum