# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
class TrieNode:
    def __init__(self):
        # Initialize a Trie node with two children (0 and 1) and a flag to mark the end of a number
        self.children = [None, None]
        self.end = False

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Create the root of the Trie
        root = TrieNode()
        
        # Insert all numbers into the Trie
        for num in nums:
            node = root
            # Convert the number to binary and iterate over each bit
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                # If the bit is not in the Trie, create a new node
                if node.children[bit] is None:
                    node.children[bit] = TrieNode()
                # Move to the next node
                node = node.children[bit]
            # Mark the end of the number
            node.end = True
        
        # Initialize the maximum XOR
        max_xor = 0
        
        # Iterate over all numbers to find the maximum XOR
        for num in nums:
            node = root
            # Initialize the current XOR
            curr_xor = 0
            # Convert the number to binary and iterate over each bit
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                # Try to find the opposite bit in the Trie to maximize the XOR
                opposite_bit = 1 - bit
                if node.children[opposite_bit] is not None:
                    # If the opposite bit is found, update the current XOR
                    curr_xor = (curr_xor << 1) | 1
                    node = node.children[opposite_bit]
                else:
                    # If the opposite bit is not found, move to the next node
                    curr_xor = curr_xor << 1
                    node = node.children[bit]
            # Update the maximum XOR
            max_xor = max(max_xor, curr_xor)
        
        return max_xor