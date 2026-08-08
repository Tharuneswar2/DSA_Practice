# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def twoOutOfThree(nums1, nums2, nums3):
    # Convert the input lists to sets for efficient lookups
    set1 = set(nums1)
    set2 = set(nums2)
    set3 = set(nums3)
    
    # Initialize a set to store the common elements
    common = set()
    
    # Find the common elements between the first two sets
    common.update(set1.intersection(set2))
    
    # Find the common elements between the first and third sets
    common.update(set1.intersection(set3))
    
    # Find the common elements between the second and third sets
    common.update(set2.intersection(set3))
    
    # Return the common elements as a list
    return list(common)