def largestGoodInteger(num: str) -> str:
    # Initialize an empty string to store the result
    result = ""

    # Initialize a variable to store the maximum length of the same digit
    max_length = 0

    # Initialize a variable to store the current digit
    current_digit = ""

    # Initialize a variable to store the count of the current digit
    current_count = 0

    # Iterate over the string
    for i in range(len(num)):
        # If the current digit is the same as the previous one, increment the count
        if i > 0 and num[i] == num[i - 1]:
            current_count += 1
        # If the current digit is different from the previous one, reset the count
        else:
            current_digit = num[i]
            current_count = 1

        # If the count of the current digit is 3 and it's greater than the max length, update the result
        if current_count == 3 and int(current_digit) > int(result) if result else True:
            result = current_digit * 3
            max_length = 3

    # Return the result
    return result