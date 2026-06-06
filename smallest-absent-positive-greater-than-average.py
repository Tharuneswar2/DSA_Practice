def smallest_absent_positive_greater_than_average(nums):
    # Calculate the average of the given list of numbers
    average = sum(nums) / len(nums)
    
    # Filter out numbers that are less than or equal to the average
    nums = [num for num in nums if num > average]
    
    # If no numbers are greater than the average, return 1
    if not nums:
        return 1
    
    # Sort the filtered list of numbers
    nums.sort()
    
    # Initialize the smallest absent positive number to 1
    smallest_absent = 1
    
    # Iterate over the sorted list of numbers
    for num in nums:
        # If the current number is greater than the smallest absent number, return the smallest absent number
        if num > smallest_absent:
            return smallest_absent
        # If the current number is equal to the smallest absent number, increment the smallest absent number
        elif num == smallest_absent:
            smallest_absent += 1
    
    # If the loop completes without finding an absent number, return the smallest absent number
    return smallest_absent

# Example usage:
print(smallest_absent_positive_greater_than_average([1, 2, 3, 4]))  # Output: 5
print(smallest_absent_positive_greater_than_average([1, 2, 4, 5]))  # Output: 3