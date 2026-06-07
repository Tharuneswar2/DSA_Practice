def count_pairs_with_sum_less_than_target(arr, target):
    # Sort the array in ascending order
    arr.sort()
    
    # Initialize two pointers, one at the start and one at the end of the array
    left = 0
    right = len(arr) - 1
    
    # Initialize a variable to store the count of pairs
    count = 0
    
    # Traverse the array using the two pointers
    while left < right:
        # If the sum of the values at the two pointers is less than the target, 
        # increment the left pointer and add the difference between the right and left pointers to the count
        if arr[left] + arr[right] < target:
            count += right - left
            left += 1
        # If the sum is not less than the target, decrement the right pointer
        else:
            right -= 1
    
    # Return the count of pairs
    return count

# Example usage:
arr = [1, 2, 3, 4, 5]
target = 7
print(count_pairs_with_sum_less_than_target(arr, target))