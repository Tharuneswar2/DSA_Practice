def find_min_common_value(nums1, nums2):
    # Create a set from the second list for efficient lookups
    set2 = set(nums2)
    
    # Initialize the minimum common value to infinity
    min_common_value = float('inf')
    
    # Iterate over the first list
    for num in nums1:
        # Check if the current number exists in the second list
        if num in set2:
            # Update the minimum common value if the current number is smaller
            min_common_value = min(min_common_value, num)
    
    # Return the minimum common value if it's not infinity, otherwise return -1
    return min_common_value if min_common_value != float('inf') else -1

# Example usage:
nums1 = [2, 1, 3]
nums2 = [1, 3, 5]
print(find_min_common_value(nums1, nums2))  # Output: 1