# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def find_missing_elements(nums):
    # First, we sort the list of numbers in ascending order
    nums.sort()
    
    # Initialize an empty list to store the missing elements
    missing_elements = []
    
    # Iterate over the sorted list of numbers
    for i in range(len(nums) - 1):
        # For each pair of adjacent numbers, calculate the difference
        diff = nums[i + 1] - nums[i]
        
        # If the difference is greater than 1, it means there are missing elements
        if diff > 1:
            # Calculate the number of missing elements
            num_missing = diff - 1
            
            # Generate the missing elements and add them to the list
            missing_elements.extend(range(nums[i] + 1, nums[i] + num_missing + 1))
    
    # Return the list of missing elements
    return missing_elements

# Example usage:
nums = [1, 2, 4, 6, 3, 7, 8]
print(find_missing_elements(nums))  # Output: [5]