# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def arrayRankTransform(arr):
    # Create a copy of the input array and sort it in ascending order
    sorted_arr = sorted(arr)
    
    # Initialize an empty dictionary to store the rank of each element
    rank_dict = {}
    
    # Iterate over the sorted array and assign a rank to each unique element
    for i, num in enumerate(sorted_arr):
        # If the number is not already in the dictionary, add it with its rank
        if num not in rank_dict:
            rank_dict[num] = i + 1
    
    # Initialize an empty list to store the transformed array
    transformed_arr = []
    
    # Iterate over the input array and replace each element with its rank
    for num in arr:
        # Append the rank of the current number to the transformed array
        transformed_arr.append(rank_dict[num])
    
    # Return the transformed array
    return transformed_arr