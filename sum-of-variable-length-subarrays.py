# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def sumOfVariableLengthSubarrays(arr):
    # Initialize the total sum as 0
    total_sum = 0
    
    # Iterate over the array with two nested loops to generate all possible subarrays
    for i in range(len(arr)): 
        # Initialize the current subarray sum as 0
        subarray_sum = 0
        
        # Generate all possible subarrays starting from index i
        for j in range(i, len(arr)):
            # Add the current element to the subarray sum
            subarray_sum += arr[j]
            
            # Add the subarray sum to the total sum
            total_sum += subarray_sum
    
    # Return the total sum
    return total_sum