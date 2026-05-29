def convertTime(current: str, correct: str) -> int:
    # Split the input strings into hours and minutes
    curr_h, curr_m = map(int, current.split(':'))
    corr_h, corr_m = map(int, correct.split(':'))

    # Calculate the total minutes for both times
    curr_total_m = curr_h * 60 + curr_m
    corr_total_m = corr_h * 60 + corr_m

    # Calculate the absolute difference in minutes
    diff_m = abs(curr_total_m - corr_total_m)

    # Calculate the minimum number of operations (60-minute turns)
    min_ops = diff_m // 60

    # Add the remaining minutes as operations
    min_ops += diff_m % 60

    return min_ops