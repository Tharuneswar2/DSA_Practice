def countEven(num: int) -> int:
    # Initialize count of numbers with even digit sum
    count = 0
    
    # Iterate over all numbers from 1 to num
    for i in range(1, num + 1):
        # Calculate the sum of digits of the current number
        digit_sum = sum(int(digit) for digit in str(i))
        
        # Check if the sum of digits is even
        if digit_sum % 2 == 0:
            # If the sum of digits is even, increment the count
            count += 1
    
    # Return the count of numbers with even digit sum
    return count