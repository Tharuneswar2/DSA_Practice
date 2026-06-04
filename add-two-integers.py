class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    # Create a dummy node to simplify some corner cases such as a list with only one node
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    # While there are still nodes in either list or a carry from the previous addition
    while l1 or l2 or carry:
        # Get the values of the current nodes in both lists, default to 0 if the list has ended
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        
        # Calculate the sum of the current nodes and the carry
        sum = carry + x + y
        
        # Update the carry for the next iteration
        carry = sum // 10
        
        # Create a new node with the digit value of the sum
        current.next = ListNode(sum % 10)
        
        # Move to the next node in both lists
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    # Return the next node of the dummy node, which is the start of the result list
    return dummy.next