# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def finalPrices(prices):
    # Initialize an empty stack to store indices of prices
    stack = []
    
    # Iterate over the prices list
    for i in range(len(prices)):
        # While the stack is not empty and the current price is less than the price at the top of the stack
        while stack and prices[i] <= prices[stack[-1]]:
            # Pop the top of the stack (index of the price that has a discount)
            idx = stack.pop()
            # Update the price at the popped index by subtracting the current price
            prices[idx] -= prices[i]
        # Push the current index onto the stack
        stack.append(i)
    
    # Return the updated prices list
    return prices