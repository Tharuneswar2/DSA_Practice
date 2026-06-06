def kConcatenationMaxSum(arr, k):
    # Calculate the total sum of the array
    total_sum = sum(arr)
    
    # Calculate the maximum sum of a subarray within the array
    max_sum = kadane(arr)
    
    # If k is 1, return the maximum sum of a subarray
    if k == 1:
        return max_sum
    
    # If the total sum is positive, it means the array has a positive contribution to the overall sum
    # In this case, we can add the total sum (k-2) times to the maximum sum of a subarray
    if total_sum > 0:
        return max_sum + total_sum * (k-2)
    
    # If the total sum is not positive, we can't add it to the maximum sum
    # In this case, we return the maximum sum of a subarray
    return max_sum


def kadane(arr):
    # Initialize the maximum sum and the current sum to the first element of the array
    max_sum = current_sum = arr[0]
    
    # Iterate over the array starting from the second element
    for num in arr[1:]:
        # Update the current sum to be the maximum of the current number and the sum of the current number and the previous current sum
        current_sum = max(num, current_sum + num)
        
        # Update the maximum sum to be the maximum of the current maximum sum and the current sum
        max_sum = max(max_sum, current_sum)
    
    # Return the maximum sum
    return max_sum