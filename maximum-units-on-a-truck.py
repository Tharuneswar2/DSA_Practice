def maximumUnits(boxTypes, truckSize):
    # Sort the box types in descending order of units per box
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the total units and the current box index
    total_units = 0
    box_index = 0
    
    # Iterate over the sorted box types
    while box_index < len(boxTypes) and truckSize > 0:
        # Calculate the number of boxes that can be loaded
        num_boxes = min(truckSize, boxTypes[box_index][0])
        
        # Update the total units and the truck size
        total_units += num_boxes * boxTypes[box_index][1]
        truckSize -= num_boxes
        
        # Move to the next box type
        box_index += 1
    
    return total_units