def fillCups(self, amount: list[int]) -> int:
    # Create a max heap from the given list
    amount = [-x for x in amount]
    import heapq
    heapq.heapify(amount)

    # Initialize the time variable
    time = 0

    # Continue the process until the heap is not empty
    while len(amount) > 1:
        # Extract the two largest elements from the heap
        first = -heapq.heappop(amount)
        second = -heapq.heappop(amount)

        # If both elements are greater than 1, push them back to the heap after decrementing
        if first > 1 and second > 1:
            heapq.heappush(amount, -first + 1)
            heapq.heappush(amount, -second + 1)
        # If only one element is greater than 1, push it back to the heap after decrementing
        elif first > 1:
            heapq.heappush(amount, -first + 1)
        elif second > 1:
            heapq.heappush(amount, -second + 1)

        # Increment the time
        time += 1

    # If there is one element left in the heap, add it to the time
    if amount:
        time += -amount[0]

    return time