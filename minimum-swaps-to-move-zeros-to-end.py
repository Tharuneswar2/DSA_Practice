def min_swaps_to_move_zeros_to_end(arr):
    # Initialize variables to keep track of the number of zeros and the number of swaps
    zeros = 0
    swaps = 0
    
    # Iterate over the array to count the number of zeros
    for num in arr:
        if num == 0:
            zeros += 1
    
    # Initialize two pointers, one at the beginning and one at the end of the array
    left = 0
    right = len(arr) - 1
    
    # Iterate over the array from left to right
    while left < right:
        # If the left element is zero, increment the left pointer
        if arr[left] == 0:
            left += 1
        # If the right element is non-zero, decrement the right pointer
        elif arr[right] != 0:
            right -= 1
        # If the left element is non-zero and the right element is zero, swap them and increment the swaps counter
        else:
            arr[left], arr[right] = arr[right], arr[left]
            swaps += 1
            left += 1
            right -= 1
    
    # The minimum number of swaps is the minimum between the number of swaps and the number of zeros
    return min(swaps, zeros)

# Test the function
arr = [1, 0, 1, 0, 1]
print(min_swaps_to_move_zeros_to_end(arr))