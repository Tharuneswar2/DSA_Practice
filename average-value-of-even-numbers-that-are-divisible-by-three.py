def average_of_even_numbers_divisible_by_three(numbers):
    # Initialize sum and count variables to zero
    total_sum = 0
    count = 0
    
    # Iterate over each number in the input list
    for num in numbers:
        # Check if the number is even and divisible by three
        if num % 2 == 0 and num % 3 == 0:
            # Add the number to the total sum
            total_sum += num
            # Increment the count of numbers that meet the condition
            count += 1
    
    # Check if any numbers met the condition
    if count == 0:
        # If not, return zero as per the problem statement
        return 0
    else:
        # Otherwise, return the average of the numbers that met the condition
        return total_sum / count

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 9, 12, 15, 18]
print(average_of_even_numbers_divisible_by_three(numbers))