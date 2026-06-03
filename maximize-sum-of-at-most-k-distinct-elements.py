from collections import Counter
from heapq import *

def maximizeSum(nums, k):
    # Count the frequency of each number
    count = Counter(nums)
    
    # Create a min heap to store the frequency of numbers
    min_heap = []
    for num, freq in count.items():
        heappush(min_heap, (freq, num))
    
    # While the heap size is greater than k, remove the smallest frequency number
    while len(min_heap) > k:
        heappop(min_heap)
    
    # Calculate the sum of the remaining numbers in the heap
    total_sum = 0
    for freq, num in min_heap:
        total_sum += freq * num
    
    return total_sum

def maximizeSumAlternative(nums, k):
    # Count the frequency of each number
    count = Counter(nums)
    
    # Sort the frequency of numbers in descending order
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    # Calculate the sum of the k most frequent numbers
    total_sum = 0
    for i in range(min(k, len(sorted_count))):
        total_sum += sorted_count[i][1] * sorted_count[i][0]
    
    return total_sum