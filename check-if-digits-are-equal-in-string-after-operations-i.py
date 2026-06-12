def digits_count(s):
    count = {}
    for char in s:
        if char.isdigit():
            count[char] = count.get(char, 0) + 1
    return count

def check_equal_digits_after_operations_I(s):
    # Count the frequency of each digit in the string
    count = digits_count(s)
    
    # Check if all digits have the same frequency
    return len(set(count.values())) == 1

# Test the function
print(check_equal_digits_after_operations_I("a2b2c2"))  # True
print(check_equal_digits_after_operations_I("a2b3c2"))  # False