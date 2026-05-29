def separate_digits(arr):
    # Initialize two lists to store even and odd digits
    even_digits = []
    odd_digits = []

    # Iterate over each number in the array
    for num in arr:
        # Convert the number to a string to easily access each digit
        str_num = str(num)
        
        # Iterate over each digit in the number
        for digit in str_num:
            # Convert the digit back to an integer
            int_digit = int(digit)
            
            # Check if the digit is even or odd
            if int_digit % 2 == 0:
                # If even, append to the even_digits list
                even_digits.append(int_digit)
            else:
                # If odd, append to the odd_digits list
                odd_digits.append(int_digit)

    # Return the lists of even and odd digits
    return even_digits, odd_digits

# Example usage:
arr = [123, 456, 789]
even, odd = separate_digits(arr)
print("Even digits:", even)
print("Odd digits:", odd)