class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def findMaximumXOR(self, nums):
        root = TrieNode()
        max_len = len(bin(max(nums))) - 2
        
        # Insert all numbers into the Trie
        for num in nums:
            node = root
            binary = bin(num)[2:].zfill(max_len)
            for bit in binary:
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
        
        max_xor = 0
        # Find the maximum XOR for each number
        for num in nums:
            node = root
            binary = bin(num)[2:].zfill(max_len)
            curr_xor = ''
            for bit in binary:
                opposite = '1' if bit == '0' else '0'
                if opposite in node.children:
                    curr_xor += '1'
                    node = node.children[opposite]
                else:
                    curr_xor += '0'
                    node = node.children[bit]
            max_xor = max(max_xor, int(curr_xor, 2))
        
        return max_xor