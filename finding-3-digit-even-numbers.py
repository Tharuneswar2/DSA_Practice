def find_even_numbers(digits):
    # Initialize an empty list to store the even numbers
    even_numbers = []

    # Iterate over each digit in the input list
    for i in range(len(digits)):
        for j in range(len(digits)):
            for k in range(len(digits)):
                # Skip if the digits are the same (to avoid duplicates)
                if i == j or i == k or j == k:
                    continue
                # Construct the 3-digit number
                num = int(str(digits[i]) + str(digits[j]) + str(digits[k]))
                # Check if the number is even
                if num % 2 == 0:
                    # Append the even number to the list
                    even_numbers.append(num)

    # Return the list of even numbers
    return even_numbers

# Example usage:
digits = [1, 2, 3, 4, 5, 6]
even_numbers = find_even_numbers(digits)
print(even_numbers)