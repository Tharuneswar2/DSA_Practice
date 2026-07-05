def account_balance_after_rounded_purchase(balance, purchase_amount):
    # Calculate the rounded purchase amount
    rounded_purchase_amount = round(purchase_amount)
    
    # Check if the rounded purchase amount is greater than the balance
    if rounded_purchase_amount > balance:
        # If it is, return the balance as it is
        return balance
    else:
        # If not, subtract the rounded purchase amount from the balance
        return balance - rounded_purchase_amount

# Test the function
balance = 100.0
purchase_amount = 25.75
print(account_balance_after_rounded_purchase(balance, purchase_amount))