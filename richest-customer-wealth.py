def maximumWealth(accounts):
    # Initialize the maximum wealth to 0
    max_wealth = 0
    
    # Iterate over each customer's accounts
    for customer in accounts:
        # Calculate the total wealth of the current customer
        customer_wealth = sum(customer)
        
        # Update the maximum wealth if the current customer's wealth is higher
        max_wealth = max(max_wealth, customer_wealth)
    
    # Return the maximum wealth found
    return max_wealth

# Example usage:
accounts = [[1,2,3],[3,2,1]]
print(maximumWealth(accounts))  # Output: 6

accounts = [[1,5],[7,3],[3,5]]
print(maximumWealth(accounts))  # Output: 10

accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(maximumWealth(accounts))  # Output: 17