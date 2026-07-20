# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def is_harshad(n):
    # Calculate the sum of digits of the number
    sum_of_digits = sum(int(digit) for digit in str(n))
    
    # Check if the number is divisible by the sum of its digits
    if n % sum_of_digits == 0:
        # If divisible, return True indicating it's a Harshad number
        return True
    else:
        # If not divisible, return False indicating it's not a Harshad number
        return False

def get_harshad_numbers(start, end):
    # Initialize an empty list to store Harshad numbers
    harshad_numbers = []
    
    # Iterate over the range from start to end (inclusive)
    for num in range(start, end + 1):
        # Check if the current number is a Harshad number
        if is_harshad(num):
            # If it's a Harshad number, append it to the list
            harshad_numbers.append(num)
    
    # Return the list of Harshad numbers
    return harshad_numbers

# Example usage:
start_range = 1
end_range = 100
print(get_harshad_numbers(start_range, end_range))