def arrayRankTransform(arr):
    # Create a sorted copy of the array to get the ranks
    sorted_arr = sorted(arr)
    
    # Create a dictionary to store the rank of each number
    rank_dict = {val: i + 1 for i, val in enumerate(sorted_arr)}
    
    # Replace each number in the original array with its rank
    return [rank_dict[val] for val in arr]