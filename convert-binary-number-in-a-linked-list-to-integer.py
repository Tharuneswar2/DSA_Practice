# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getDecimalValue(head):
    # Initialize the result variable to store the decimal value
    decimal_value = 0
    
    # Traverse the linked list
    while head:
        # Left shift the current decimal value by 1 bit to make space for the new bit
        decimal_value = decimal_value << 1
        
        # Add the value of the current node to the decimal value
        decimal_value += head.val
        
        # Move to the next node in the linked list
        head = head.next
    
    # Return the decimal value
    return decimal_value