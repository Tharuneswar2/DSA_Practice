# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def count_pairs(nums, target):
    # Sort the array in ascending order to efficiently find pairs
    nums.sort()
    
    # Initialize two pointers, one at the start and one at the end of the array
    left, right = 0, len(nums) - 1
    
    # Initialize a variable to store the count of pairs
    count = 0
    
    # Traverse the array using the two pointers
    while left < right:
        # If the sum of the values at the two pointers is less than the target, 
        # it means all pairs with the left pointer will have a sum less than the target
        if nums[left] + nums[right] < target:
            # Increment the count by the number of pairs that can be formed with the left pointer
            count += right - left
            # Move the left pointer to the right to find more pairs
            left += 1
        else:
            # If the sum is not less than the target, move the right pointer to the left
            right -= 1
    
    # Return the count of pairs
    return count