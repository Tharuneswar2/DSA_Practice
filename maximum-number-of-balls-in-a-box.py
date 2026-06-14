def countBalls(lowLimit: int, highLimit: int) -> int:
    # Create a dictionary to store the count of balls in each box
    box_count = {}
    
    # Initialize the maximum count of balls in a box
    max_count = 0
    
    # Iterate over the range from lowLimit to highLimit (inclusive)
    for num in range(lowLimit, highLimit + 1):
        # Calculate the sum of digits of the current number
        box_index = sum(int(digit) for digit in str(num))
        
        # Increment the count of balls in the current box
        box_count[box_index] = box_count.get(box_index, 0) + 1
        
        # Update the maximum count of balls in a box
        max_count = max(max_count, box_count[box_index])
    
    # Return the maximum count of balls in a box
    return max_count