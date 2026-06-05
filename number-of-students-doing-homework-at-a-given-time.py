def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def busyStudent(startTime, endTime, queryTime):
    count = 0
    for start, end in zip(startTime, endTime):
        if start <= queryTime <= end:
            count += 1
    return count

def busyStudentOptimized(startTime, endTime, queryTime):
    # Combine start and end times into a list of tuples
    times = list(zip(startTime, endTime))
    
    # Sort the times based on the start time
    times.sort(key=lambda x: x[0])
    
    # Initialize two pointers, one at the start and one at the end
    left, right = 0, len(times) - 1
    
    # Find the first start time that is greater than the query time
    while left <= right:
        mid = (left + right) // 2
        if times[mid][0] <= queryTime:
            left = mid + 1
        else:
            right = mid - 1
    
    # The number of students doing homework is the number of start times less than or equal to the query time
    count = left
    
    # Find the first end time that is greater than the query time
    left, right = 0, len(times) - 1
    while left <= right:
        mid = (left + right) // 2
        if times[mid][1] <= queryTime:
            left = mid + 1
        else:
            right = mid - 1
    
    # The number of students not doing homework is the number of end times less than or equal to the query time
    not_doing_homework = left
    
    # The number of students doing homework is the total number of students minus the number of students not doing homework
    return count - not_doing_homework

def busyStudentOptimized2(startTime, endTime, queryTime):
    # Combine start and end times into a list of tuples
    times = list(zip(startTime, endTime))
    
    # Sort the times based on the start time
    times.sort(key=lambda x: x[0])
    
    # Find the first start time that is greater than the query time
    start_index = binarySearch([time[0] for time in times], queryTime)
    
    # Find the first end time that is greater than the query time
    end_index = binarySearch([time[1] for time in times], queryTime)
    
    # The number of students doing homework is the number of start times less than or equal to the query time
    # minus the number of end times less than or equal to the query time
    return start_index - end_index

# Test the functions
startTime = [1, 2, 3]
endTime = [2, 3, 4]
queryTime = 3
print(busyStudent(startTime, endTime, queryTime))  # Output: 1
print(busyStudentOptimized(startTime, endTime, queryTime))  # Output: 1
print(busyStudentOptimized2(startTime, endTime, queryTime))  # Output: 1