def coupon_validator(coupon, min_amount, max_discount):
    # Check if coupon is a string
    if not isinstance(coupon, str):
        return False
    
    # Check if min_amount and max_discount are integers
    if not isinstance(min_amount, int) or not isinstance(max_discount, int):
        return False
    
    # Check if min_amount and max_discount are within valid range
    if min_amount < 0 or max_discount < 0 or max_discount > 100:
        return False
    
    # Check if coupon is in the correct format (e.g., 'COUPON-1234')
    if not coupon.startswith('COUPON-') or len(coupon) != 11:
        return False
    
    # Extract the coupon code
    code = coupon[7:]
    
    # Check if the coupon code is numeric
    if not code.isnumeric():
        return False
    
    # If all checks pass, the coupon is valid
    return True

def calculate_discount(amount, coupon, min_amount, max_discount):
    # Check if the coupon is valid
    if not coupon_validator(coupon, min_amount, max_discount):
        return 0
    
    # Check if the amount is greater than or equal to the minimum amount
    if amount < min_amount:
        return 0
    
    # Calculate the discount
    discount = (amount / 100) * max_discount
    
    # Return the discount
    return discount

# Example usage:
coupon = 'COUPON-1234'
min_amount = 100
max_discount = 20
amount = 200

if coupon_validator(coupon, min_amount, max_discount):
    discount = calculate_discount(amount, coupon, min_amount, max_discount)
    print(f'The discount is: {discount}')
else:
    print('Invalid coupon')