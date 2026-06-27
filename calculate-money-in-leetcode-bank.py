def totalMoney(n: int) -> int:
    # Calculate the number of full weeks
    full_weeks = n // 7
    
    # Calculate the remaining days
    remaining_days = n % 7
    
    # Calculate the total money for full weeks
    # Each week, the money increases by 1, so the total money for a week is the sum of an arithmetic series
    # The sum of an arithmetic series can be calculated as (n * (a1 + an)) / 2, where n is the number of terms, a1 is the first term, and an is the last term
    # In this case, the first term is 1 and the last term is the number of the week
    total_money_full_weeks = (full_weeks * (full_weeks + 1)) // 2 * 7
    
    # Calculate the total money for the remaining days
    # The money for the remaining days is the sum of an arithmetic series with the first term being the number of the first day of the remaining days and the last term being the number of the last day of the remaining days
    # The number of the first day of the remaining days is the number of the last day of the last full week plus 1
    # The number of the last day of the last full week is the number of the week
    # The number of the week is the number of full weeks
    total_money_remaining_days = (remaining_days * (full_weeks + 1 + full_weeks + remaining_days)) // 2
    
    # Return the total money
    return total_money_full_weeks + total_money_remaining_days