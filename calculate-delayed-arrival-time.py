def calculate_delayed_arrival_time(departure_time, travel_time, delay):
    # Convert departure time to minutes
    departure_hours, departure_minutes = map(int, departure_time.split(':'))
    departure_time_in_minutes = departure_hours * 60 + departure_minutes
    
    # Calculate arrival time in minutes
    arrival_time_in_minutes = departure_time_in_minutes + travel_time
    
    # Add delay to arrival time
    delayed_arrival_time_in_minutes = arrival_time_in_minutes + delay
    
    # Convert delayed arrival time back to hours and minutes
    delayed_arrival_hours = delayed_arrival_time_in_minutes // 60
    delayed_arrival_minutes = delayed_arrival_time_in_minutes % 60
    
    # Format delayed arrival time as a string
    delayed_arrival_time = f"{delayed_arrival_hours}:{delayed_arrival_minutes:02d}"
    
    return delayed_arrival_time

# Example usage:
departure_time = "08:30"
travel_time = 120  # in minutes
delay = 15  # in minutes
print(calculate_delayed_arrival_time(departure_time, travel_time, delay))