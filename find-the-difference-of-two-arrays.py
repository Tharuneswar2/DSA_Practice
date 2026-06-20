def find_difference(nums1, nums2):
    # Convert the input lists to sets for efficient lookups
    set1 = set(nums1)
    set2 = set(nums2)

    # Find the elements that are in set1 but not in set2
    diff1 = set1 - set2

    # Find the elements that are in set2 but not in set1
    diff2 = set2 - set1

    # Return the differences as lists
    return list(diff1), list(diff2)

# Example usage:
nums1 = [1, 2, 3]
nums2 = [2, 4, 5]
diff1, diff2 = find_difference(nums1, nums2)
print("Elements in nums1 but not in nums2:", diff1)
print("Elements in nums2 but not in nums1:", diff2)