# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def separate_digits(nums):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over each number in the input list
    for num in nums:
        # Convert the number to a string to easily separate the digits
        str_num = str(num)
        
        # Iterate over each character (digit) in the string
        for digit in str_num:
            # Append the integer value of the digit to the result list
            result.append(int(digit))
    
    # Return the result list
    return result