def twoOutOfThree(nums1, nums2, nums3):
    # Convert the input lists to sets for efficient lookups
    set1 = set(nums1)
    set2 = set(nums2)
    set3 = set(nums3)

    # Initialize a set to store the common elements
    common = set()

    # Find the common elements between each pair of sets
    common.update(set1 & set2)
    common.update(set1 & set3)
    common.update(set2 & set3)

    # Return the common elements as a list
    return list(common)

# Test the function
print(twoOutOfThree([1, 1, 3, 2], [2, 3], [3]))
print(twoOutOfThree([3, 1], [2, 3], [1, 2]))