# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def reformatDate(date):
    # Split the date string into day, month, and year
    day, month, year = date.split(' ')
    
    # Create a dictionary to map month names to their corresponding numbers
    month_map = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
        "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
        "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }
    
    # Remove the comma and the 'th', 'st', 'nd', 'rd' suffix from the day
    day = day[:-2]
    
    # Format the day to have two digits
    if len(day) == 1:
        day = '0' + day
    
    # Replace the month name with its corresponding number
    month = month_map[month]
    
    # Return the reformatted date in the format 'year-month-day'
    return f'{year}-{month}-{day}'