# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def distinctAverages(nums):
    # Create a set to store unique averages, using a set automatically eliminates duplicates
    averages = set()
    
    # Sort the list in ascending order
    nums.sort()
    
    # Initialize two pointers, one at the start and one at the end of the list
    left, right = 0, len(nums) - 1
    
    # Continue the process until the two pointers meet
    while left < right:
        # Calculate the average of the values at the current pointers
        avg = (nums[left] + nums[right]) / 2
        
        # Add the average to the set
        averages.add(avg)
        
        # Move the pointers closer to each other
        left += 1
        right -= 1
    
    # Return the number of unique averages
    return len(averages)