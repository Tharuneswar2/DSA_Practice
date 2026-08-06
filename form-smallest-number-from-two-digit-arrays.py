# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def minNumber(nums1, nums2):
    # Combine the two lists into one
    combined = nums1 + nums2
    
    # Sort the combined list in ascending order
    combined.sort()
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the combined list
    for num in combined:
        # Convert the number to a string and add it to the result
        result += str(num)
        
        # If the length of the result is 2, break the loop
        if len(result) == 2:
            break
            
    # If the length of the result is still less than 2, 
    # it means the two lists do not have any common digits
    if len(result) < 2:
        # Find the smallest number in the first list
        min_num1 = min(nums1)
        
        # Find the smallest number in the second list
        min_num2 = min(nums2)
        
        # Compare the two smallest numbers and return the smaller one
        result = str(min(min_num1, min_num2)) + str(max(min_num1, min_num2))
        
    # Return the result
    return int(result)