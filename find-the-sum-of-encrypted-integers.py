# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def findEncryptedSum(nums):
    # Initialize the sum of encrypted integers to 0
    encrypted_sum = 0
    
    # Iterate over each number in the input list
    for num in nums:
        # Convert the integer to a string to easily access each digit
        str_num = str(num)
        
        # Initialize the encrypted number to 0
        encrypted_num = 0
        
        # Iterate over each digit in the number
        for digit in str_num:
            # Add the ASCII value of the digit to the encrypted number
            # The ASCII value of a digit is the digit itself plus 48 (for '0' to '9')
            encrypted_num += ord(digit)
        
        # Add the encrypted number to the total sum
        encrypted_sum += encrypted_num
    
    # Return the total sum of encrypted integers
    return encrypted_sum