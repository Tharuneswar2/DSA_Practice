def smallest_even_multiple(n):
    # The smallest even multiple of a number is the number itself if it's even, 
    # otherwise it's the number multiplied by 2
    if n % 2 == 0:
        return n
    else:
        return n * 2

# Test the function
print(smallest_even_multiple(5))  # Output: 10
print(smallest_even_multiple(10))  # Output: 10