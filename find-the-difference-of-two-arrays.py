# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def find_difference(nums1, nums2):
    # Convert the input lists to sets for efficient lookups
    set1 = set(nums1)
    set2 = set(nums2)

    # Use set difference operation to find elements in set1 but not in set2
    diff1 = set1 - set2
    
    # Use set difference operation to find elements in set2 but not in set1
    diff2 = set2 - set1
    
    # Return the differences as lists
    return list(diff1), list(diff2)

# Example usage
nums1 = [1, 2, 3]
nums2 = [2, 4, 5]
print(find_difference(nums1, nums2))