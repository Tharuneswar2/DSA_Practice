# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def maximumCount(nums):
    # Initialize two pointers, one at the start and one at the end of the array
    left, right = 0, len(nums) - 1
    
    # Initialize the count of positive and negative integers
    positive_count, negative_count = 0, 0
    
    # Traverse the array from both ends
    while left <= right:
        # If the left element is negative, increment the negative count and move the left pointer
        if nums[left] < 0:
            negative_count += 1
            left += 1
        # If the right element is positive, increment the positive count and move the right pointer
        elif nums[right] > 0:
            positive_count += 1
            right -= 1
        # If the left element is 0, move the left pointer
        elif nums[left] == 0:
            left += 1
        # If the right element is 0, move the right pointer
        else:
            right -= 1
    
    # Return the maximum count of positive and negative integers
    return max(positive_count, negative_count)