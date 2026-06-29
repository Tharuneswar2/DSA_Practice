def countGoodTriplets(arr, a, b, c):
    # Initialize count of good triplets
    count = 0
    
    # Iterate over all possible triplets in the array
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                # Check if the current triplet satisfies the given conditions
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    # If the conditions are satisfied, increment the count
                    count += 1
                    
    # Return the total count of good triplets
    return count

# Test the function
arr = [3, 0, 1, 1, 9, 9]
a = 2
b = 1
c = 1
print(countGoodTriplets(arr, a, b, c))