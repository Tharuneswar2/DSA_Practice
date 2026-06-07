def countUnequalTriplets(arr):
    # Initialize count of unequal triplets
    count = 0
    
    # Iterate over all possible triplets in the array
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                # Check if the current triplet is unequal
                if arr[i] != arr[j] and arr[i] != arr[k] and arr[j] != arr[k]:
                    # Increment the count of unequal triplets
                    count += 1
                    
    # Return the total count of unequal triplets
    return count

# Test the function
arr = [1, 2, 3, 4, 5]
print(countUnequalTriplets(arr))