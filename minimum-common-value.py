# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def minimumCommonValue(nums1, nums2):
    # Create a set from the second list for efficient lookups
    set2 = set(nums2)
    
    # Initialize the minimum common value to infinity
    min_common = float('inf')
    
    # Iterate over the first list
    for num in nums1:
        # Check if the current number exists in the second list
        if num in set2:
            # Update the minimum common value if the current number is smaller
            min_common = min(min_common, num)
            # If we found a common value, we can break the loop
            if min_common != float('inf'):
                break
    
    # Return the minimum common value if found, otherwise return -1
    return min_common if min_common != float('inf') else -1