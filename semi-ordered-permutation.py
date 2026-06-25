def semiOrderedPermutation(arr):
    # Initialize variables to store the indices of the smallest and largest elements
    smallest = 0
    largest = 0
    
    # Find the indices of the smallest and largest elements
    for i in range(len(arr)):
        if arr[i] == 1:
            smallest = i
        elif arr[i] == len(arr):
            largest = i
    
    # Swap the smallest element with the first element
    arr[0], arr[smallest] = arr[smallest], arr[0]
    
    # Swap the largest element with the last element
    arr[-1], arr[largest] = arr[largest], arr[-1]
    
    # Initialize variables to store the indices of the next smallest and next largest elements
    next_smallest = 1
    next_largest = len(arr) - 2
    
    # Initialize variables to store the values of the next smallest and next largest elements
    val = len(arr) - 1
    
    # Rearrange the elements in the middle
    for i in range(1, len(arr) - 1):
        if next_smallest <= next_largest:
            if arr[i] < arr[next_smallest]:
                next_smallest += 1
            elif arr[i] > arr[next_largest]:
                next_largest -= 1
            else:
                if val > len(arr) // 2:
                    arr[next_smallest], arr[i] = arr[i], arr[next_smallest]
                    next_smallest += 1
                else:
                    arr[next_largest], arr[i] = arr[i], arr[next_largest]
                    next_largest -= 1
                val -= 1
        else:
            break
    
    return arr

# Test the function
print(semiOrderedPermutation([4, 3, 2, 6, 5, 1]))