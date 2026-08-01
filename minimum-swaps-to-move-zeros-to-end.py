# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minSwapsToMoveZerosToEnd(arr):
    # Initialize variables to store the total number of zeros and the number of swaps required
    total_zeros = 0
    swaps_required = 0
    
    # Count the total number of zeros in the array
    for num in arr:
        if num == 0:
            total_zeros += 1
    
    # Initialize two pointers, one at the beginning and one at the end of the array
    left = 0
    right = len(arr) - 1
    
    # Traverse the array from left to right
    while left < right:
        # If the left element is zero, increment the left pointer
        if arr[left] == 0:
            left += 1
        # If the right element is non-zero, decrement the right pointer
        elif arr[right] != 0:
            right -= 1
        # If the left element is non-zero and the right element is zero, swap them and increment the swaps required
        else:
            arr[left], arr[right] = arr[right], arr[left]
            swaps_required += 1
            left += 1
            right -= 1
    
    # Return the minimum number of swaps required to move all zeros to the end
    return swaps_required