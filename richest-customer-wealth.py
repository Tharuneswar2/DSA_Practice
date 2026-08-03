# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maximumWealth(accounts):
    # Initialize max_wealth to store the maximum wealth found so far
    max_wealth = 0
    
    # Iterate over each customer's accounts
    for customer_accounts in accounts:
        # Calculate the total wealth of the current customer by summing up all their account balances
        customer_wealth = sum(customer_accounts)
        
        # Update max_wealth if the current customer's wealth is greater
        max_wealth = max(max_wealth, customer_wealth)
    
    # Return the maximum wealth found
    return max_wealth