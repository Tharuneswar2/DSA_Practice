# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def calculate_tax(income, tax_brackets):
    # Initialize total tax paid to 0
    total_tax = 0
    
    # Initialize previous tax bracket upper limit to 0
    prev_upper_limit = 0
    
    # Iterate over each tax bracket
    for bracket in tax_brackets:
        # Extract lower and upper limits of the current tax bracket
        lower_limit, upper_limit, tax_rate = bracket
        
        # Calculate the income that falls within the current tax bracket
        income_in_bracket = min(upper_limit, income) - prev_upper_limit
        
        # If income in the current bracket is positive, calculate tax for this bracket
        if income_in_bracket > 0:
            # Calculate tax for the current bracket
            tax_in_bracket = income_in_bracket * tax_rate
            
            # Add tax for the current bracket to the total tax
            total_tax += tax_in_bracket
        
        # Update previous tax bracket upper limit
        prev_upper_limit = upper_limit
        
        # If income is less than or equal to the upper limit of the current bracket, break the loop
        if income <= upper_limit:
            break
    
    # Return the total tax paid
    return total_tax

# Example usage:
tax_brackets = [(0, 9875, 0.10), (9876, 40125, 0.12), (40126, 85525, 0.22), (85526, 163300, 0.24), (163301, 207350, 0.32), (207351, 518400, 0.35), (518401, float('inf'), 0.37)]
income = 50000
print(calculate_tax(income, tax_brackets))