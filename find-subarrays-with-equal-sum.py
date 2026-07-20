# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def find_subarrays_with_equal_sum(arr):
    # Initialize an empty dictionary to store the cumulative sum and its frequency
    cumulative_sum_freq = {0: 1}  # Initialize with 0 sum having frequency 1
    
    # Initialize variables to store the cumulative sum and the result
    cumulative_sum = 0
    result = []
    
    # Iterate over the array
    for i in range(len(arr)):
        # Update the cumulative sum
        cumulative_sum += arr[i]
        
        # Check if the cumulative sum minus the target sum exists in the dictionary
        for target_sum in range(cumulative_sum + 1):
            if cumulative_sum - target_sum in cumulative_sum_freq:
                # If it exists, append the subarray to the result
                result.extend([arr[j:i+1] for j in range(len(arr)) if sum(arr[j:i+1]) == target_sum])
        
        # Update the frequency of the cumulative sum
        cumulative_sum_freq[cumulative_sum] = cumulative_sum_freq.get(cumulative_sum, 0) + 1
    
    # Return the result
    return result

def find_subarrays_with_equal_sum_k(arr, k):
    # Initialize an empty dictionary to store the cumulative sum and its frequency
    cumulative_sum_freq = {0: 1}  # Initialize with 0 sum having frequency 1
    
    # Initialize variables to store the cumulative sum and the result
    cumulative_sum = 0
    result = []
    
    # Iterate over the array
    for i in range(len(arr)):
        # Update the cumulative sum
        cumulative_sum += arr[i]
        
        # Check if the cumulative sum minus the target sum exists in the dictionary
        if cumulative_sum - k in cumulative_sum_freq:
            # If it exists, append the subarray to the result
            result.append(arr[i - cumulative_sum_freq[cumulative_sum - k] + 1:i+1])
        
        # Update the frequency of the cumulative sum
        cumulative_sum_freq[cumulative_sum] = cumulative_sum_freq.get(cumulative_sum, 0) + 1
    
    # Return the result
    return result