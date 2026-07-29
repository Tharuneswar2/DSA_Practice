# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def largestRectangleArea(heights):
    # Initialize a stack to store indices of the heights array
    stack = []
    
    # Initialize the maximum area
    max_area = 0
    
    # Initialize the index
    index = 0
    
    # Traverse the heights array
    while index < len(heights):
        # If the stack is empty or the current height is greater than the height at the top of the stack, push the index to the stack
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            # If the current height is less than the height at the top of the stack, calculate the area
            top_of_stack = stack.pop()
            
            # Calculate the width
            width = index if not stack else index - stack[-1] - 1
            
            # Calculate the area
            area = heights[top_of_stack] * width
            
            # Update the maximum area
            max_area = max(max_area, area)
    
    # Calculate the area for the remaining heights in the stack
    while stack:
        top_of_stack = stack.pop()
        
        # Calculate the width
        width = index if not stack else len(heights) - stack[-1] - 1
        
        # Calculate the area
        area = heights[top_of_stack] * width
        
        # Update the maximum area
        max_area = max(max_area, area)
    
    # Return the maximum area
    return max_area