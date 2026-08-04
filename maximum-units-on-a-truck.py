# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def maximumUnits(boxTypes, truckSize):
    # Sort the boxTypes in descending order based on the number of units per box
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the total units to 0
    total_units = 0
    
    # Iterate over each box type
    for boxes, units in boxTypes:
        # If the truck size is greater than or equal to the number of boxes, 
        # add the total units to the total and subtract the boxes from the truck size
        if truckSize >= boxes:
            total_units += boxes * units
            truckSize -= boxes
        # If the truck size is less than the number of boxes, 
        # add the remaining truck size times the units to the total and break the loop
        else:
            total_units += truckSize * units
            break
    
    # Return the total units
    return total_units