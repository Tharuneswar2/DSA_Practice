# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def find_missing_repeated(nums):
    # Create a set to store the numbers we've seen so far
    seen = set()
    # Create a list to store the duplicates
    duplicates = []
    # Create a list to store the missing numbers
    missing = []
    
    # Iterate over the range from 1 to the length of the input list + 1
    for num in range(1, len(nums) + 1):
        # If the number is not in the input list, add it to the missing list
        if num not in nums:
            missing.append(num)
    
    # Iterate over the input list
    for num in nums:
        # If the number is already in the seen set, it's a duplicate
        if num in seen:
            duplicates.append(num)
        # Otherwise, add it to the seen set
        else:
            seen.add(num)
    
    # Return the missing and duplicate numbers
    return missing, duplicates

# Test the function
nums = [4, 3, 2, 7, 8, 2, 3, 1]
missing, duplicates = find_missing_repeated(nums)
print("Missing numbers:", missing)
print("Duplicate numbers:", duplicates)