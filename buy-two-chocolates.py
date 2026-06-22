def buy_two_chocolates(candies, cost):
    # Sort the candies in ascending order
    candies.sort()
    
    # Initialize two pointers, one at the start and one at the end
    left = 0
    right = len(candies) - 1
    
    # Continue the loop until the two pointers meet
    while left < right:
        # Calculate the total cost of the two chocolates
        total_cost = candies[left] + candies[right]
        
        # If the total cost is equal to the cost of two chocolates, return True
        if total_cost == cost:
            return True
        # If the total cost is less than the cost of two chocolates, move the left pointer to the right
        elif total_cost < cost:
            left += 1
        # If the total cost is greater than the cost of two chocolates, move the right pointer to the left
        else:
            right -= 1
    
    # If no two chocolates can be bought, return False
    return False

# Test the function
candies = [1, 2, 3, 4, 5]
cost = 7
print(buy_two_chocolates(candies, cost))  # Output: True