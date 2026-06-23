def increasing_subarrays(nums):
    # Initialize variables to track the current and maximum length of increasing subarrays
    current_length = 1
    max_length = 1
    
    # Iterate over the array from the second element to the end
    for i in range(1, len(nums)):
        # If the current element is greater than the previous one, it can be part of the current increasing subarray
        if nums[i] > nums[i - 1]:
            # Increase the length of the current increasing subarray
            current_length += 1
        else:
            # If the current element is not greater than the previous one, update the maximum length if necessary
            max_length = max(max_length, current_length)
            # Reset the length of the current increasing subarray
            current_length = 1
    
    # Update the maximum length one last time after the loop
    max_length = max(max_length, current_length)
    
    return max_length

def adjacent_increasing_subarrays(nums):
    # Initialize variables to track the start and end indices of the longest increasing subarray
    start = 0
    end = 0
    max_length = 0
    
    # Iterate over the array
    for i in range(len(nums)):
        # Initialize variables to track the current length of increasing subarray
        current_length = 1
        
        # Iterate over the array from the current element to the end
        for j in range(i + 1, len(nums)):
            # If the current element is greater than the previous one, it can be part of the current increasing subarray
            if nums[j] > nums[j - 1]:
                # Increase the length of the current increasing subarray
                current_length += 1
            else:
                # If the current element is not greater than the previous one, break the loop
                break
        
        # If the length of the current increasing subarray is greater than the maximum length, update the maximum length and the start and end indices
        if current_length > max_length:
            max_length = current_length
            start = i
            end = i + max_length - 1
    
    # Return the longest increasing subarray
    return nums[start:end + 1]

# Test the functions
nums = [1, 2, 3, 4, 5, 2, 3, 4, 5, 6]
print(increasing_subarrays(nums))
print(adjacent_increasing_subarrays(nums))