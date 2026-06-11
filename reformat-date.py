def reformatDate(date):
    # Split the date string into day, month, and year
    day, month, year = date.split(' ')
    
    # Create a dictionary to map month names to their corresponding numbers
    month_map = {
        'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 
        'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 
        'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
    }
    
    # Remove the suffix from the day (e.g., 'st', 'nd', 'rd', 'th')
    day = day[:-2]
    
    # Format the day to have two digits (e.g., '1' becomes '01')
    day = day.zfill(2)
    
    # Return the reformatted date in the format 'year-month-day'
    return f'{year}-{month_map[month]}-{day}'