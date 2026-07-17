# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def dayOfTheWeek(day: int, month: int, year: int) -> str:
    # Define the days of the week as a list
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    # Define the months with their respective number of days in a non-leap year
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Calculate the total number of days from the year 1971 to the given year
    total_days = (year - 1971) * 365 + (year - 1971) // 4 - (year - 1971) // 100 + (year - 1971) // 400
    
    # Check if the year is a leap year and adjust the total days accordingly
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        total_days += 1
    
    # Calculate the total number of days from January to the given month
    for i in range(1, month):
        total_days += months[i]
    
    # If the month is February and the year is a leap year, add one more day
    if month > 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        total_days += 1
    
    # Add the given day to the total days
    total_days += day
    
    # Calculate the day of the week by taking the modulus of the total days with 7
    day_of_week = total_days % 7
    
    # Return the day of the week
    return days[day_of_week]