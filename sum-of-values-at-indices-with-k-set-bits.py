def sum_of_indices_with_k_set_bits(nums, k):
    def count_set_bits(n):
        # Count the number of set bits in a number
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

    total_sum = 0
    for i, num in enumerate(nums):
        # Check if the number of set bits in the index is equal to k
        if count_set_bits(i) == k:
            # If true, add the value at the index to the total sum
            total_sum += num

    return total_sum