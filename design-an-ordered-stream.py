class OrderedStream:

    def __init__(self, n: int):
        # Initialize an empty list to store the stream values
        self.stream = [None] * (n + 1)
        # Initialize the pointer to the first empty slot
        self.ptr = 0

    def insert(self, id: int, value: str) -> list[str]:
        # Store the value at the corresponding index
        self.stream[id] = value
        # Initialize the result list
        result = []
        # While the current pointer points to a non-empty slot
        while self.stream[self.ptr]:
            # Append the value at the current pointer to the result list
            result.append(self.stream[self.ptr])
            # Move the pointer to the next slot
            self.ptr += 1
        # Return the result list
        return result