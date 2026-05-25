def is_harshad_number(n):
    # Calculate the sum of digits of the number
    sum_of_digits = sum(int(digit) for digit in str(n))
    
    # Check if the number is divisible by the sum of its digits
    if n % sum_of_digits == 0:
        return True
    else:
        return False

def get_harshad_numbers_in_range(start, end):
    # Initialize an empty list to store Harshad numbers
    harshad_numbers = []
    
    # Iterate over the range of numbers
    for num in range(start, end + 1):
        # Check if the number is a Harshad number
        if is_harshad_number(num):
            # If it is, add it to the list
            harshad_numbers.append(num)
    
    return harshad_numbers

# Example usage
start_range = 1
end_range = 100
print(get_harshad_numbers_in_range(start_range, end_range))