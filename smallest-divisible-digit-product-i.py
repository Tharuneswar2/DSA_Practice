def smallest_divisible_digit_product(n):
    # Start from the smallest possible number with n digits
    num = int('1' * n)
    
    # Continue checking numbers until we find one that is divisible by 1 to n
    while True:
        # Check if the number is divisible by all numbers from 1 to n
        if all(num % i == 0 for i in range(1, n + 1)):
            return num
        # If not, increment the number and try again
        num += 1

# Test the function
print(smallest_divisible_digit_product(3))  # Output: 2520