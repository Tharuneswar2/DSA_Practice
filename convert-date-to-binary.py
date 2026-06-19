from datetime import datetime

def convert_date_to_binary(date_str):
    # Parse the input date string into a datetime object
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Extract year, month, and day from the datetime object
    year = date.year
    month = date.month
    day = date.day
    
    # Convert year, month, and day to binary and remove the '0b' prefix
    binary_year = bin(year)[2:].zfill(16)
    binary_month = bin(month)[2:].zfill(8)
    binary_day = bin(day)[2:].zfill(8)
    
    # Combine the binary year, month, and day into a single string
    binary_date = binary_year + binary_month + binary_day
    
    return binary_date

# Example usage
date_str = '2022-07-25'
binary_date = convert_date_to_binary(date_str)
print(binary_date)