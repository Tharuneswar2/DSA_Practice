def find_missing_elements(nums):
    # Create a set from the input list for efficient lookups
    num_set = set(nums)
    
    # Find the minimum and maximum values in the list
    min_val = min(nums)
    max_val = max(nums)
    
    # Initialize an empty list to store the missing elements
    missing_elements = []
    
    # Iterate over the range from the minimum to the maximum value
    for i in range(min_val, max_val + 1):
        # If the current number is not in the set, it's a missing element
        if i not in num_set:
            missing_elements.append(i)
    
    return missing_elements

# Example usage:
nums = [1, 2, 3, 5, 6, 8, 9]
print(find_missing_elements(nums))  # Output: [4, 7]