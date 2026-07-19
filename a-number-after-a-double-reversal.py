# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def is_same_after_reversals(num: int) -> bool:
    # Convert the number into a string to easily reverse it
    str_num = str(num)
    
    # Reverse the string representation of the number
    reversed_str_num = str_num[::-1]
    
    # Convert the reversed string back into an integer
    reversed_num = int(reversed_str_num)
    
    # Reverse the reversed number
    reversed_reversed_str_num = str(reversed_num)[::-1]
    
    # Convert the reversed reversed string back into an integer
    reversed_reversed_num = int(reversed_reversed_str_num)
    
    # Check if the original number is equal to the number after double reversal
    return num == reversed_reversed_num