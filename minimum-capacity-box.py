# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def minCapacityBox(boxes, units):
    # Initialize the minimum capacity to positive infinity
    min_capacity = float('inf')
    
    # Iterate over each box in the list of boxes
    for box in boxes:
        # Calculate the capacity of the current box
        capacity = box[0] * box[1] * box[2]
        
        # If the capacity of the current box is less than the minimum capacity and can hold all units
        if capacity < min_capacity and capacity >= units:
            # Update the minimum capacity
            min_capacity = capacity
    
    # If no box can hold all units, return -1
    if min_capacity == float('inf'):
        return -1
    else:
        # Return the minimum capacity
        return min_capacity