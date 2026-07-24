# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countGoodTriplets(arr, a, b, c):
    # Initialize count of good triplets to 0
    count = 0
    
    # Iterate over all possible triplets in the array
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                # Check if the absolute difference between the elements at indices i, j, k and a, b, c respectively is less than or equal to 1
                if (abs(arr[i] - a) <= 1) and (abs(arr[j] - b) <= 1) and (abs(arr[k] - c) <= 1):
                    # If the condition is met, increment the count of good triplets
                    count += 1
                    
    # Return the total count of good triplets
    return count