# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def unique_3_digit_even_numbers():
    # Initialize an empty set to store unique 3-digit even numbers
    unique_numbers = set()
    
    # Iterate over all possible hundreds digits (1-9)
    for hundreds in range(1, 10):
        # Iterate over all possible tens digits (0-9)
        for tens in range(10):
            # Iterate over all possible ones digits that result in an even number (0, 2, 4, 6, 8)
            for ones in range(0, 10, 2):
                # Construct the 3-digit number
                number = hundreds * 100 + tens * 10 + ones
                # Add the number to the set
                unique_numbers.add(number)
    
    # Return the total count of unique 3-digit even numbers
    return len(unique_numbers)

print(unique_3_digit_even_numbers())