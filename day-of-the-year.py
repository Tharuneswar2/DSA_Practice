# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def dayOfYear(date: str) -> int:
    # Split the input string into year, month, and day
    year, month, day = map(int, date.split('-'))
    
    # Define the number of days in each month for non-leap years
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        # If it's a leap year, February has 29 days
        days_in_month[1] = 29
    
    # Calculate the total number of days before the current month
    total_days = sum(days_in_month[:month-1])
    
    # Add the current day to the total number of days
    total_days += day
    
    # Return the total number of days
    return total_days