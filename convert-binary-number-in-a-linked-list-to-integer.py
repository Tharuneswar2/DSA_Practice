# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # Initialize result variable to store the decimal value
        result = 0
        
        # Traverse the linked list
        while head:
            # Left shift the bits of result by 1 and add the current node's value
            # This is equivalent to multiplying the result by 2 and adding the current bit
            result = (result << 1) | head.val
            
            # Move to the next node in the linked list
            head = head.next
        
        # Return the decimal value
        return result