# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def specialArray(nums):
    # First, sort the array in ascending order
    nums.sort()
    
    # Initialize two pointers, one at the start and one at the end of the array
    left, right = 0, len(nums)
    
    # Continue the loop until the two pointers meet
    while left < right:
        # Calculate the middle index
        mid = (left + right + 1) // 2
        
        # If the number of elements greater than or equal to 'mid' is equal to 'mid', return 'mid'
        if sum(1 for num in nums if num >= mid) == mid:
            return mid
        
        # If the number of elements greater than or equal to 'mid' is less than 'mid', move the left pointer to 'mid'
        elif sum(1 for num in nums if num >= mid) < mid:
            right = mid - 1
        
        # If the number of elements greater than or equal to 'mid' is greater than 'mid', move the left pointer to 'mid'
        else:
            left = mid
    
    # If no such 'mid' is found, return -1
    return -1