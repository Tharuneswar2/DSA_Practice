def alternating_groups(arr):
    # Initialize variables to track the current group and its size
    current_group = arr[0]
    current_group_size = 1
    max_group_size = 1

    # Iterate over the array starting from the second element
    for i in range(1, len(arr)):
        # If the current element is the same as the current group, increment the group size
        if arr[i] == current_group:
            current_group_size += 1
        # If the current element is different from the current group, update the max group size and reset the current group
        else:
            max_group_size = max(max_group_size, current_group_size)
            current_group = arr[i]
            current_group_size = 1

    # Update the max group size one last time after the loop ends
    max_group_size = max(max_group_size, current_group_size)

    return max_group_size

def alternating_groups_i(arr):
    # Initialize variables to track the current group and its size
    current_group = arr[0]
    current_group_size = 1
    max_group_size = 1
    prev_group = None

    # Iterate over the array starting from the second element
    for i in range(1, len(arr)):
        # If the current element is the same as the current group, increment the group size
        if arr[i] == current_group:
            current_group_size += 1
        # If the current element is different from the current group, update the max group size and reset the current group
        else:
            # If the current group is the same as the previous group, reset the current group size
            if current_group == prev_group:
                current_group_size = 1
            else:
                max_group_size = max(max_group_size, current_group_size)
            prev_group = current_group
            current_group = arr[i]
            current_group_size = 1

    # Update the max group size one last time after the loop ends
    max_group_size = max(max_group_size, current_group_size)

    return max_group_size