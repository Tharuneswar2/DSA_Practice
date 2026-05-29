def max_output(nums):
    # Initialize variables to store the concatenated non-zero digits and their sum
    non_zero_digits = ''
    sum_of_digits = 0

    # Iterate over each number in the input list
    for num in nums:
        # Convert the number to a string to easily access its digits
        str_num = str(num)
        
        # Iterate over each digit in the number
        for digit in str_num:
            # Check if the digit is non-zero
            if digit != '0':
                # Append the non-zero digit to the concatenated string
                non_zero_digits += digit
                # Add the non-zero digit to the sum
                sum_of_digits += int(digit)

    # If there are no non-zero digits, return 0
    if sum_of_digits == 0:
        return 0

    # Multiply the concatenated non-zero digits by their sum
    result = int(non_zero_digits) * sum_of_digits

    return result