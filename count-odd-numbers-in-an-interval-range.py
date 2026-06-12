def countOdds(low: int, high: int) -> int:
    # Calculate the total number of integers in the range
    total_numbers = high - low + 1
    
    # If the total number of integers is odd, then the number of odd integers is half of the total plus one
    # If the total number of integers is even, then the number of odd integers is half of the total
    # But we need to consider the case when the low number is odd or even
    # If the low number is odd, then the number of odd integers is half of the total plus one
    # If the low number is even, then the number of odd integers is half of the total
    
    # So, we can use the formula: (total_numbers + 1) // 2 if low is odd, otherwise total_numbers // 2
    # We can use the fact that low % 2 == 1 if low is odd, and low % 2 == 0 if low is even
    # So, we can use the formula: (total_numbers + low % 2) // 2
    
    return (total_numbers + low % 2) // 2