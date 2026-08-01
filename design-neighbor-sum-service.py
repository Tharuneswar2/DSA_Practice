# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

class NeighborSumService:
    def __init__(self, nums):
        # Initialize the service with a list of numbers
        self.nums = nums
        # Create a prefix sum array to store the cumulative sum of the numbers
        self.prefix_sum = [0] * (len(nums) + 1)
        # Calculate the prefix sum
        for i in range(len(nums)):
            # The prefix sum at index i is the sum of all numbers up to index i
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def query(self, left, right):
        # Calculate the sum of the numbers in the range [left, right] using the prefix sum array
        # The sum is the difference between the prefix sum at index right + 1 and the prefix sum at index left
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

    def update(self, index, val):
        # Update the number at index to val
        # Calculate the difference between the new value and the old value
        diff = val - self.nums[index]
        # Update the prefix sum array by adding the difference to all elements after index
        for i in range(index + 1, len(self.prefix_sum)):
            self.prefix_sum[i] += diff
        # Update the number at index to val
        self.nums[index] = val