# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def transformArray(arr):
    # Initialize an empty list to store the transformed array
    transformed_arr = []
    
    # Iterate over each element in the input array
    for i in range(len(arr)):
        # If the current element is the first element or it's different from the previous one, 
        # append it to the transformed array as is
        if i == 0 or arr[i] != arr[i-1]:
            transformed_arr.append(arr[i])
        # If the current element is the same as the previous one, 
        # append the previous element plus one to the transformed array
        else:
            transformed_arr.append(arr[i-1] + 1)
    
    # Return the transformed array
    return transformed_arr