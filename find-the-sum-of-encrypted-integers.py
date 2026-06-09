def find_sum_of_encrypted_integers(nums):
    # Initialize the sum of encrypted integers to 0
    encrypted_sum = 0
    
    # Iterate over each number in the input list
    for num in nums:
        # Convert the number to binary and remove the '0b' prefix
        binary_num = bin(num)[2:]
        
        # Calculate the encrypted integer by summing the digits of the binary representation
        encrypted_num = sum(int(digit) for digit in binary_num)
        
        # Add the encrypted integer to the total sum
        encrypted_sum += encrypted_num
    
    # Return the total sum of encrypted integers
    return encrypted_sum

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = find_sum_of_encrypted_integers(numbers)
print(result)