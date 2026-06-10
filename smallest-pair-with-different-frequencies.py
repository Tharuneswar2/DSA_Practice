from collections import Counter

def smallest_pair_with_different_frequencies(nums):
    # Count the frequency of each number
    freq = Counter(nums)
    
    # Initialize the minimum difference and the pair
    min_diff = float('inf')
    pair = ()
    
    # Iterate over the frequency dictionary
    for num1, count1 in freq.items():
        for num2, count2 in freq.items():
            # Check if the frequencies are different
            if count1 != count2:
                # Calculate the absolute difference between the numbers
                diff = abs(num1 - num2)
                # Update the minimum difference and the pair if necessary
                if diff < min_diff:
                    min_diff = diff
                    pair = (num1, num2)
    
    return pair

# Example usage:
nums = [1, 2, 3, 4, 5, 2, 3, 3]
print(smallest_pair_with_different_frequencies(nums))