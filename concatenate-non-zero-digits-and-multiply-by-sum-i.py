# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def getConcatenationSum(nums):
    # Initialize an empty string to store the concatenated non-zero digits
    concatenated_str = ""
    
    # Initialize a variable to store the sum of non-zero digits
    sum_of_digits = 0
    
    # Iterate over each number in the input list
    for num in nums:
        # Convert the number to a string to easily access each digit
        str_num = str(num)
        
        # Iterate over each digit in the number
        for digit in str_num:
            # Check if the digit is non-zero
            if digit != '0':
                # Concatenate the non-zero digit to the string
                concatenated_str += digit
                
                # Add the non-zero digit to the sum
                sum_of_digits += int(digit)
    
    # Convert the concatenated string to an integer
    concatenated_int = int(concatenated_str)
    
    # Return the product of the concatenated integer and the sum of non-zero digits
    return concatenated_int * sum_of_digits