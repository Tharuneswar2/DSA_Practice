# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def removeAnagrams(words):
    # Initialize an empty stack to store the result
    stack = []
    
    # Iterate over each word in the input list
    for word in words:
        # If the stack is empty or the top of the stack is not an anagram of the current word, push the word to the stack
        if not stack or sorted(stack[-1]) != sorted(word):
            stack.append(word)
    
    # Return the stack as the result
    return stack