def targetIndices(nums, target):
    # Count the number of elements less than the target
    less_than_target = sum(1 for num in nums if num < target)
    
    # Count the number of elements equal to the target
    equal_to_target = nums.count(target)
    
    # The target indices will be from the count of elements less than the target
    # to the count of elements less than the target plus the count of elements equal to the target
    return list(range(less_than_target, less_than_target + equal_to_target))