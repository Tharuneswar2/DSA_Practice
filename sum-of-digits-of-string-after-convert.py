def getSum(s: str, k: int) -> int:
    # Convert the string into a list of integers
    nums = [int(i) for i in s]
    
    # Calculate the sum of the digits
    total_sum = sum(nums)
    
    # Multiply the sum by k
    total_sum *= k
    
    # Convert the total sum into a string to calculate the sum of its digits
    total_sum_str = str(total_sum)
    
    # Initialize a variable to store the sum of the digits
    sum_of_digits = 0
    
    # Calculate the sum of the digits
    for digit in total_sum_str:
        sum_of_digits += int(digit)
    
    # Return the sum of the digits
    return sum_of_digits