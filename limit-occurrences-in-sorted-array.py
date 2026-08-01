# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def limit_occurrences(nums, limit):
    # Initialize an empty dictionary to store the count of each number
    count_dict = {}
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list
    for num in nums:
        # If the number is already in the dictionary, increment its count
        if num in count_dict:
            count_dict[num] += 1
        # If the number is not in the dictionary, add it with a count of 1
        else:
            count_dict[num] = 1
        
        # If the count of the current number is less than or equal to the limit, add it to the result
        if count_dict[num] <= limit:
            result.append(num)
    
    # Return the result
    return result