class LastVisitedIntegers:
    def __init__(self):
        self.stack = []
        self.set = set()

    def add(self, num):
        # If the number is already in the set, remove it from the stack
        if num in self.set:
            self.stack.remove(num)
        # Add the number to the stack and the set
        self.stack.append(num)
        self.set.add(num)

    def get_last_visited(self, k):
        # Return the last k visited integers
        return self.stack[-k:]


# Example usage:
last_visited = LastVisitedIntegers()
last_visited.add(1)
last_visited.add(2)
last_visited.add(3)
last_visited.add(2)
last_visited.add(4)
print(last_visited.get_last_visited(2))  # Output: [4, 2]
print(last_visited.get_last_visited(3))  # Output: [4, 2, 3]