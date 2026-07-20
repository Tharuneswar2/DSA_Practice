# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def check_sorted_and_rotated(nums):
    # Check if the input list is empty
    if not nums:
        return False
    
    # Find the number of rotations by finding the index of the minimum element
    rotations = nums.index(min(nums))
    
    # Split the list into two parts at the rotation point
    first_part = nums[rotations:]
    second_part = nums[:rotations]
    
    # Check if the first part is sorted in ascending order
    if first_part != sorted(first_part):
        return False
    
    # Check if the second part is sorted in ascending order
    if second_part != sorted(second_part):
        return False
    
    # If both parts are sorted, check if the last element of the second part is less than the first element of the first part
    if second_part and first_part and second_part[-1] > first_part[0]:
        return False
    
    # If all conditions are met, the array is sorted and rotated
    return True