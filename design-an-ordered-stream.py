# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

class OrderedStream:

    def __init__(self):
        # Initialize an empty list to store the stream values
        self.stream = []
        # Initialize a pointer to keep track of the current index
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        # Insert the value at the correct index in the stream list
        self.stream[id - 1] = value
        # Initialize an empty list to store the result
        res = []
        # While the value at the current pointer index is not None
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            # Append the value at the current pointer index to the result list
            res.append(self.stream[self.ptr])
            # Increment the pointer
            self.ptr += 1
        # Return the result list
        return res