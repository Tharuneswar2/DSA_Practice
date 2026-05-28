def check_sorted_and_rotated(nums):
    # If the array is empty or contains only one element, it's considered sorted and rotated
    if len(nums) <= 1:
        return True

    # Find the number of rotations by finding the index of the minimum element
    rotations = nums.index(min(nums))

    # Rotate the array back to its original position
    original = nums[rotations:] + nums[:rotations]

    # Check if the original array is sorted
    return original == sorted(original)

# Test the function
print(check_sorted_and_rotated([3, 4, 5, 1, 2]))  # True
print(check_sorted_and_rotated([1, 2, 3, 4, 5]))  # True
print(check_sorted_and_rotated([5, 1, 2, 3, 4]))  # True
print(check_sorted_and_rotated([1, 3, 2, 4, 5]))  # False