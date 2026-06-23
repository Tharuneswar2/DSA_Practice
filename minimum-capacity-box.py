def minimum_capacity_box(weights, boxes):
    # Sort the weights in descending order
    weights.sort(reverse=True)
    
    # Sort the boxes in descending order
    boxes.sort(reverse=True)
    
    # Initialize the minimum capacity
    min_capacity = 0
    
    # Iterate over the weights and boxes
    for weight, box in zip(weights, boxes):
        # Update the minimum capacity
        min_capacity = max(min_capacity, (weight + box - 1) // box)
    
    return min_capacity

# Example usage:
weights = [3, 2, 1]
boxes = [2, 2, 1]
print(minimum_capacity_box(weights, boxes))