def sort_array_by_parity(nums):
    # Initialize two pointers, one at the start and one at the end of the array
    left, right = 0, len(nums) - 1
    
    # Continue the process until the two pointers meet
    while left < right:
        # If the left element is even, move to the next element
        if nums[left] % 2 == 0:
            left += 1
        # If the right element is odd, move to the previous element
        elif nums[right] % 2 != 0:
            right -= 1
        # If the left element is odd and the right element is even, swap them
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    return nums

# Alternatively, you can use a more Pythonic way to solve this problem
def sort_array_by_parity_pythonic(nums):
    # Separate the even and odd numbers into two lists
    even = [num for num in nums if num % 2 == 0]
    odd = [num for num in nums if num % 2 != 0]
    
    # Combine the two lists to get the final result
    return even + odd