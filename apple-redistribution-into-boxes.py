def min_operations(apples, boxes):
    # Sort the apples in descending order
    apples.sort(reverse=True)
    
    # Initialize the boxes with the maximum capacity
    boxes.sort(reverse=True)
    
    # Initialize the count of operations
    operations = 0
    
    # Iterate over the apples
    for i, apple in enumerate(apples):
        # If the apple can fit into the current box, add it
        if apple <= boxes[i % len(boxes)]:
            boxes[i % len(boxes)] -= apple
        # If the apple cannot fit into the current box, add it to the next box
        else:
            operations += 1
            boxes[(i + 1) % len(boxes)] -= apple
    
    return operations

# Test the function
apples = [3, 4, 1, 2]
boxes = [5, 5]
print(min_operations(apples, boxes))