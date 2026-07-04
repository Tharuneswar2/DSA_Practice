def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights = [0] + heights + [0]
    
    # Iterate over the heights array
    for i in range(len(heights)):
        # While the stack is not empty and the current height is less than the height at the top of the stack
        while stack and heights[i] < heights[stack[-1]]:
            # Get the height at the top of the stack
            h = heights[stack.pop()]
            # Get the width of the rectangle
            w = i - stack[-1] - 1
            # Update the max area
            max_area = max(max_area, h * w)
        # Push the current index to the stack
        stack.append(i)
    
    return max_area

def maximalRectangle(matrix):
    if not matrix:
        return 0
    
    # Initialize the heights array with the first row of the matrix
    heights = [int(x) for x in matrix[0]]
    max_area = largestRectangleArea(heights)
    
    # Iterate over the rest of the rows in the matrix
    for row in matrix[1:]:
        # Update the heights array
        for i in range(len(row)):
            heights[i] = heights[i] + 1 if row[i] == '1' else 0
        # Update the max area
        max_area = max(max_area, largestRectangleArea(heights))
    
    return max_area