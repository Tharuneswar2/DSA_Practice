# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def binarySearch(nums, target):
    # Initialize two pointers, one at the start and one at the end of the list
    left, right = 0, len(nums) - 1
    
    # Continue the search until the two pointers meet
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # If the middle element is equal to the target, return the index
        if nums[mid] == target:
            return mid
        # If the middle element is greater than the target, move the right pointer to the left
        elif nums[mid] > target:
            right = mid - 1
        # If the middle element is less than the target, move the left pointer to the right
        else:
            left = mid + 1
            
    # If the target is not found, return the index where it should be inserted to maintain sorted order
    return left

def busyStudent(startTime, endTime, queryTime):
    # Initialize a counter to store the number of students doing homework at the query time
    count = 0
    
    # Iterate over the start and end times
    for start, end in zip(startTime, endTime):
        # Check if the query time is within the start and end time
        if start <= queryTime <= end:
            # If it is, increment the counter
            count += 1
            
    # Return the count of students doing homework at the query time
    return count

def busyStudentBinarySearch(startTime, endTime, queryTime):
    # Initialize a list to store the times when students start or end doing homework
    times = []
    
    # Iterate over the start and end times
    for start, end in zip(startTime, endTime):
        # Add the start time with a value of 1 (representing the start of homework) to the list
        times.append((start, 1))
        # Add the end time with a value of -1 (representing the end of homework) to the list
        times.append((end, -1))
        
    # Sort the list of times
    times.sort()
    
    # Initialize a counter to store the number of students doing homework at the query time
    count = 0
    
    # Iterate over the sorted list of times
    for time, value in times:
        # If the time is less than or equal to the query time, add the value to the counter
        if time <= queryTime:
            count += value
        # If the time is greater than the query time, break the loop
        else:
            break
            
    # Return the count of students doing homework at the query time
    return count