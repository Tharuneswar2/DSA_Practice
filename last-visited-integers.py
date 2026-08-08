# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
class LastVisitedIntegers:
    def __init__(self):
        # Initialize an empty dictionary to store the last visited time for each integer
        self.last_visited = {}
        # Initialize a counter to keep track of the current time
        self.time = 0

    def visit(self, integer):
        # Increment the time counter
        self.time += 1
        # Update the last visited time for the given integer
        self.last_visited[integer] = self.time

    def last_visited_integer(self):
        # Find the integer with the maximum last visited time
        return max(self.last_visited, key=self.last_visited.get)

    def last_visited_time(self, integer):
        # Return the last visited time for the given integer
        return self.last_visited.get(integer, -1)

def last_visited_integers(nums):
    # Create an instance of the LastVisitedIntegers class
    lvi = LastVisitedIntegers()
    # Iterate over the given list of integers
    for num in nums:
        # Visit each integer
        lvi.visit(num)
    # Return the last visited integer and its last visited time
    return lvi.last_visited_integer(), lvi.last_visited_time(lvi.last_visited_integer())

# Example usage
nums = [1, 2, 3, 4, 5]
last_visited_integer, last_visited_time = last_visited_integers(nums)
print(f"Last visited integer: {last_visited_integer}, Last visited time: {last_visited_time}")