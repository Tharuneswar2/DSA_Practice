# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def specialArray(nums):
    # First, sort the array in descending order to easily find the number of elements greater than or equal to x
    nums.sort(reverse=True)
    
    # Initialize the count of elements greater than or equal to x
    count = 0
    
    # Iterate over the sorted array
    for i, num in enumerate(nums):
        # If the current number is greater than or equal to its index plus one (since indices are 0-based), increment the count
        if num >= i + 1:
            count += 1
        # If the current number is less than its index plus one, break the loop since the array is sorted in descending order
        else:
            break
    
    # If the count is equal to the length of the array, return -1 since there is no such x
    if count == len(nums):
        return -1
    # Otherwise, return the count
    else:
        return count