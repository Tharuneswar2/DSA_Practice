def unique_3_digit_even_numbers(digits):
    # Initialize an empty set to store unique 3-digit even numbers
    unique_numbers = set()

    # Iterate over each digit in the input list
    for i in range(len(digits)):
        # Iterate over each digit in the input list (excluding the current digit)
        for j in range(len(digits)):
            if i != j:
                # Iterate over each digit in the input list (excluding the current two digits)
                for k in range(len(digits)):
                    if i != k and j != k:
                        # Form a 3-digit number using the current three digits
                        number = int(str(digits[i]) + str(digits[j]) + str(digits[k]))
                        # Check if the number is even and has 3 digits
                        if number % 2 == 0 and number >= 100:
                            # Add the number to the set
                            unique_numbers.add(number)

    # Return the count of unique 3-digit even numbers
    return len(unique_numbers)

# Example usage:
digits = [1, 2, 3, 4, 5, 6]
print(unique_3_digit_even_numbers(digits))