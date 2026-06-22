def sumBase(n, k):
    # Convert the number to base k
    base_k_num = ''
    while n > 0:
        # Append the remainder of n divided by k to the base k number
        base_k_num = str(n % k) + base_k_num
        # Update n to be the quotient of n divided by k
        n = n // k

    # Calculate the sum of the digits in the base k number
    sum_of_digits = 0
    for digit in base_k_num:
        # Add the integer value of the digit to the sum
        sum_of_digits += int(digit)

    return sum_of_digits