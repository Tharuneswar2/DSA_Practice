class TrieNode:
    def __init__(self):
        # Initialize a TrieNode with an empty dictionary to store children and a variable to store the word
        self.children = {}
        self.word = None

class WeightedWordMapping:
    def __init__(self):
        # Initialize the WeightedWordMapping with a TrieNode as the root
        self.root = TrieNode()

    def insert(self, word, weight):
        # Start at the root of the Trie
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the node's children, add it
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node
            node = node.children[char]
        # Store the word and its weight in the final node
        node.word = word
        node.weight = weight

    def search(self, prefix):
        # Start at the root of the Trie
        node = self.root
        # Iterate over each character in the prefix
        for char in prefix:
            # If the character is not in the node's children, return an empty list
            if char not in node.children:
                return []
            # Move to the child node
            node = node.children[char]
        # Perform a depth-first search to find all words with the given prefix
        return self._dfs(node, prefix)

    def _dfs(self, node, prefix):
        # Initialize a list to store the results
        results = []
        # If the node has a word, add it to the results
        if node.word:
            results.append((node.word, node.weight))
        # Iterate over each child node
        for child in node.children.values():
            # Recursively search the child node and add the results
            results.extend(self._dfs(child, prefix))
        # Return the results
        return results

# Example usage
mapping = WeightedWordMapping()
mapping.insert("apple", 5)
mapping.insert("app", 3)
mapping.insert("application", 10)
print(mapping.search("app"))