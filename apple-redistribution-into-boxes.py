# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def distribute_apples(apples, boxes):
    # Sort the apples in descending order to maximize the number of apples in each box
    apples.sort(reverse=True)
    
    # Initialize the boxes with 0 apples
    boxes = [0] * len(boxes)
    
    # Iterate over the apples
    for apple in apples:
        # Iterate over the boxes
        for i, box in enumerate(boxes):
            # If the current box can hold the apple, add it to the box
            if box + apple <= boxes[i]:
                boxes[i] += apple
                break
            # If the current box cannot hold the apple, try the next box
            elif i == len(boxes) - 1:
                # If no box can hold the apple, return -1
                return -1
    
    # Return the boxes with the distributed apples
    return boxes

def min_boxes(apples, max_apples_per_box):
    # Sort the apples in descending order to minimize the number of boxes
    apples.sort(reverse=True)
    
    # Initialize the number of boxes
    num_boxes = 0
    
    # Iterate over the apples
    for apple in apples:
        # If the current box is full or does not exist, create a new box
        if num_boxes == 0 or apple > max_apples_per_box - boxes[num_boxes - 1]:
            num_boxes += 1
            boxes.append(0)
        # Add the apple to the current box
        boxes[num_boxes - 1] += apple
    
    # Return the minimum number of boxes
    return num_boxes