# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def sum_of_squares(nums):
    # Initialize variables to store the result and the current sum of squares
    result = 0
    current_sum = 0
    
    # Initialize a set to store unique elements in the current subarray
    unique_elements = set()
    
    # Initialize the left pointer of the sliding window
    left = 0
    
    # Iterate over the array with the right pointer of the sliding window
    for right in range(len(nums)):
        # Add the square of the current element to the current sum
        current_sum += nums[right] ** 2
        
        # Add the current element to the set of unique elements
        unique_elements.add(nums[right])
        
        # While there are duplicate elements in the current subarray, move the left pointer to the right
        while len(unique_elements) != right - left + 1:
            # Remove the square of the leftmost element from the current sum
            current_sum -= nums[left] ** 2
            
            # Remove the leftmost element from the set of unique elements
            unique_elements.remove(nums[left])
            
            # Move the left pointer to the right
            left += 1
        
        # Add the current sum to the result
        result += current_sum
    
    # Return the result
    return result