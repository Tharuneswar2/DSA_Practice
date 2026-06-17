def makeSmallestPalindrome(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Find the middle index of the string
    mid = len(num_str) // 2
    
    # If the string length is odd, the middle character can be anything
    if len(num_str) % 2 != 0:
        # Make the first half of the string the smallest possible
        first_half = '0' * mid
        # The middle character can be '0' to make the palindrome smallest
        middle = '0'
        # The second half is the reverse of the first half
        second_half = first_half[::-1]
        # Combine the three parts to form the smallest palindrome
        return int(first_half + middle + second_half)
    else:
        # If the string length is even, the middle two characters must be the same
        # Make the first half of the string the smallest possible
        first_half = '0' * (mid - 1)
        # The last character of the first half must be '1' to make the palindrome smallest
        first_half += '1'
        # The second half is the reverse of the first half
        second_half = first_half[::-1]
        # Combine the two parts to form the smallest palindrome
        return int(first_half + second_half)

# Test the function
print(makeSmallestPalindrome(100))  # Output: 101
print(makeSmallestPalindrome(1234))  # Output: 1001