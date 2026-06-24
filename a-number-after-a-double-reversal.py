def is_same_after_reversals(num: int) -> bool:
    # Convert the number to a string to easily reverse it
    str_num = str(num)
    
    # Reverse the string
    reversed_str_num = str_num[::-1]
    
    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str_num)
    
    # Reverse the integer again
    reversed_str_num_again = str(reversed_num)[::-1]
    
    # Convert the reversed string back to an integer again
    reversed_num_again = int(reversed_str_num_again)
    
    # Check if the original number is the same as the number after double reversal
    return num == reversed_num_again