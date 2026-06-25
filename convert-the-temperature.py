def convertTemperature(celsius):
    # Convert Celsius to Fahrenheit
    fahrenheit = celsius * 9 / 5 + 32
    
    # Convert Celsius to Kelvin
    kelvin = celsius + 273.15
    
    # Return the converted temperatures
    return fahrenheit, kelvin

# Test the function
celsius = 30
fahrenheit, kelvin = convertTemperature(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F and {kelvin}K")

def convertTemperatureAlternative(celsius):
    # Convert Celsius to Fahrenheit and Kelvin in one line
    return celsius * 9 / 5 + 32, celsius + 273.15

# Test the alternative function
celsius = 30
fahrenheit, kelvin = convertTemperatureAlternative(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F and {kelvin}K")