def calculate_tax(income, tax_brackets):
    """
    Calculate the amount paid in taxes given the income and tax brackets.

    Args:
        income (float): The income to calculate taxes for.
        tax_brackets (list): A list of tuples containing the upper limit of each tax bracket and the corresponding tax rate.

    Returns:
        float: The total amount paid in taxes.
    """
    # Sort the tax brackets in ascending order based on the upper limit
    tax_brackets.sort(key=lambda x: x[0])

    # Initialize the total tax paid
    total_tax = 0

    # Initialize the previous upper limit to 0
    prev_upper_limit = 0

    # Iterate over each tax bracket
    for upper_limit, tax_rate in tax_brackets:
        # Calculate the income in the current tax bracket
        income_in_bracket = min(upper_limit, income) - prev_upper_limit

        # If the income in the current bracket is positive, calculate the tax paid in this bracket
        if income_in_bracket > 0:
            # Calculate the tax paid in the current bracket
            tax_in_bracket = income_in_bracket * tax_rate

            # Add the tax paid in the current bracket to the total tax paid
            total_tax += tax_in_bracket

        # Update the previous upper limit
        prev_upper_limit = upper_limit

        # If the income is less than or equal to the upper limit of the current bracket, break the loop
        if income <= upper_limit:
            break

    # Return the total tax paid
    return total_tax


# Example usage:
tax_brackets = [(9875, 0.10), (40125, 0.12), (85525, 0.22), (163300, 0.24), (207350, 0.32), (518400, 0.35), (float('inf'), 0.37)]
income = 50000
print(calculate_tax(income, tax_brackets))