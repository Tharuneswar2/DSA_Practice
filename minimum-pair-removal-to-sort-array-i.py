# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def minimumSwaps(nums):
    # Initialize variables to store the number of swaps and the length of the array
    swaps = 0
    n = len(nums)

    # Create a copy of the array and sort it
    # This will be used as a reference to determine the correct order of elements
    sorted_nums = sorted(nums)

    # Create a dictionary to store the indices of elements in the sorted array
    index_dict = {val: i for i, val in enumerate(sorted_nums)}

    # Iterate over the array
    for i in range(n):
        # If the current element is not in its correct position
        if nums[i] != sorted_nums[i]:
            # Get the index of the element that should be at the current position
            swap_index = index_dict[nums[i]]

            # Swap the current element with the element at the swap index
            nums[i], nums[swap_index] = nums[swap_index], nums[i]

            # Update the index dictionary
            index_dict[nums[i]], index_dict[nums[swap_index]] = index_dict[nums[swap_index]], index_dict[nums[i]]

            # Increment the swap count
            swaps += 1

    # Return the minimum number of swaps required
    return swaps