# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def daysBetweenDates(date1, date2):
    # Define the days in each month for non-leap years
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Split the input dates into year, month, and day
    year1, month1, day1 = map(int, date1.split('-'))
    year2, month2, day2 = map(int, date2.split('-'))
    
    # Initialize the total days
    total_days = 0
    
    # Calculate the total days for the years before the current year
    for year in range(min(year1, year2), max(year1, year2)):
        # Check if the year is a leap year
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            total_days += 366
        else:
            total_days += 365
    
    # Calculate the total days for the months before the current month
    for month in range(min(month1, month2), max(month1, month2)):
        # Check if the month is February and the year is a leap year
        if month == 1 and (year1 % 4 == 0 and (year1 % 100 != 0 or year1 % 400 == 0) or year2 % 4 == 0 and (year2 % 100 != 0 or year2 % 400 == 0)):
            total_days += 29
        else:
            total_days += days_in_month[month - 1]
    
    # Calculate the total days for the days before the current day
    total_days += abs(day1 - day2)
    
    # Return the total days
    return total_days