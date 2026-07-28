# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def count_subarrays(arr):
    # Initialize count variable to store the number of subarrays that satisfy the condition
    count = 0
    
    # Iterate over the array with a sliding window of size 3
    for i in range(len(arr) - 2):
        # Check if the middle element is greater than its neighbors
        if arr[i] < arr[i + 1] > arr[i + 2]:
            # If the condition is satisfied, increment the count
            count += 1
    
    # Return the total count of subarrays that satisfy the condition
    return count