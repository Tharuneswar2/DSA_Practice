from datetime import datetime

def daysBetweenDates(date1, date2):
    # Convert input strings to datetime objects
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")

    # Calculate the absolute difference between the two dates
    difference = abs(date2 - date1)

    # Return the number of days in the difference
    return difference.days

# Test the function
print(daysBetweenDates("2019-06-29", "2019-06-30"))  # Output: 1
print(daysBetweenDates("2020-01-15", "2019-12-31"))  # Output: 15