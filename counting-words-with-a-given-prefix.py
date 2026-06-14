class TrieNode:
    def __init__(self):
        # Initialize a TrieNode with an empty dictionary to store children and a count to store the number of words
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        # Initialize a Trie with a root node
        self.root = TrieNode()

    def insert(self, word):
        # Insert a word into the Trie
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.count += 1

    def count_words_with_prefix(self, prefix):
        # Count the number of words with a given prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return self._count_words(node)

    def _count_words(self, node):
        # Helper function to count the number of words in a subtree
        count = node.count
        for child in node.children.values():
            count += self._count_words(child)
        return count

def count_words_with_prefix(words, prefix):
    # Create a Trie and insert all words
    trie = Trie()
    for word in words:
        trie.insert(word)
    # Return the count of words with the given prefix
    return trie.count_words_with_prefix(prefix)

# Example usage
words = ["apple", "app", "application", "banana", "banter"]
prefix = "app"
print(count_words_with_prefix(words, prefix))  # Output: 3