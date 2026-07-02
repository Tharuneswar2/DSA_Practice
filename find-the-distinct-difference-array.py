def distinct_difference_array(nums):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list
    for i in range(len(nums)):
        # Initialize a set to store unique elements
        unique_elements = set()
        
        # Iterate over the elements to the right of the current element
        for j in range(i + 1, len(nums)):
            # Add the difference to the set
            unique_elements.add(nums[j] - nums[i])
        
        # Append the number of unique differences to the result
        result.append(len(unique_elements))
    
    return result

# Example usage
nums = [1, 2, 3, 4, 5]
print(distinct_difference_array(nums))