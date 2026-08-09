# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def find_3_digit_even_numbers():
    # Initialize an empty list to store 3-digit even numbers
    even_numbers = []

    # Iterate over all possible 3-digit numbers (100 to 999)
    for num in range(100, 1000):
        # Check if the number is even by using the modulus operator (%)
        # If the remainder of the number divided by 2 is 0, it's even
        if num % 2 == 0:
            # If the number is even, append it to the list
            even_numbers.append(num)

    # Return the list of 3-digit even numbers
    return even_numbers

# Alternatively, use list comprehension for a more concise solution
def find_3_digit_even_numbers_concise():
    # Use list comprehension to generate a list of 3-digit even numbers
    # The expression 'num for num in range(100, 1000) if num % 2 == 0' generates even numbers
    even_numbers = [num for num in range(100, 1000) if num % 2 == 0]
    return even_numbers

# Test the functions
print(find_3_digit_even_numbers())
print(find_3_digit_even_numbers_concise())