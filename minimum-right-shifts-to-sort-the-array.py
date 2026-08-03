# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def min_right_shifts_to_sort(arr):
    # Create a copy of the array and sort it to compare with the original array
    sorted_arr = sorted(arr)
    
    # Initialize the count of right shifts
    right_shifts = 0
    
    # Iterate over the array
    for i in range(len(arr)):
        # If the current element is not equal to the corresponding element in the sorted array
        if arr[i] != sorted_arr[i]:
            # Find the index of the current element in the sorted array
            idx = sorted_arr.index(arr[i])
            
            # If the index is greater than the current index, it means we need to shift the element to the right
            if idx > i:
                # Update the count of right shifts
                right_shifts += idx - i
                
                # Update the sorted array by shifting the elements to the right
                sorted_arr = sorted_arr[:i] + [sorted_arr[idx]] + sorted_arr[i:idx] + sorted_arr[idx+1:]
                
                # Decrement the index to recheck the current element
                i -= 1
                
    # Return the minimum number of right shifts required to sort the array
    return right_shifts