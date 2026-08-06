# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def findKthPositive(arr, k):
    # Initialize two pointers, one at the start of the array and one at the first positive integer
    i, num = 0, 1
    
    # Continue the loop until we find the kth missing positive number
    while k > 0:
        # If the current number is not in the array, it's a missing positive number
        if i == len(arr) or arr[i] != num:
            # Decrement k by 1 because we found a missing positive number
            k -= 1
            # If k becomes 0, return the current number as it's the kth missing positive number
            if k == 0:
                return num
        # If the current number is in the array, move to the next number in the array
        else:
            i += 1
        # Move to the next positive integer
        num += 1