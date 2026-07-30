# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countOdds(low: int, high: int) -> int:
    # Calculate the total number of integers in the range [low, high]
    total_numbers = high - low + 1
    
    # If the total number of integers is odd, then there will be one more odd number than even numbers
    # So, we calculate the number of odd numbers by doing integer division of total_numbers by 2 and adding the remainder
    # This is because in a sequence of consecutive integers, the number of odd integers is equal to the number of even integers plus one if the total count is odd
    odd_count = (total_numbers + 1) // 2
    
    # If low is even, then the first number in the range is even, so we need to subtract one from the odd count
    # This is because we have counted one extra even number as an odd number
    if low % 2 == 0:
        odd_count -= 1
    
    # Return the count of odd numbers
    return odd_count