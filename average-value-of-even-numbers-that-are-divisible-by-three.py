# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def average_of_even_numbers_divisible_by_three(nums):
    # Initialize sum and count variables to keep track of the sum and count of even numbers divisible by 3
    total_sum = 0
    count = 0
    
    # Iterate over each number in the input list
    for num in nums:
        # Check if the number is even and divisible by 3
        if num % 2 == 0 and num % 3 == 0:
            # If the number is even and divisible by 3, add it to the total sum
            total_sum += num
            # Increment the count of even numbers divisible by 3
            count += 1
    
    # Check if there are any even numbers divisible by 3
    if count == 0:
        # If not, return 0 as the average
        return 0
    else:
        # If there are, return the average of the even numbers divisible by 3
        return total_sum / count