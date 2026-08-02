# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def convertTemperature(celsius):
    # Define the conversion factors for Fahrenheit and Kelvin
    fahrenheit_conversion_factor = 9/5
    kelvin_conversion_factor = 273.15
    
    # Convert Celsius to Fahrenheit
    fahrenheit = celsius * fahrenheit_conversion_factor + 32
    
    # Convert Celsius to Kelvin
    kelvin = celsius + kelvin_conversion_factor
    
    # Return the converted temperatures as a list
    return [fahrenheit, kelvin]

def main():
    # Test the function with a sample input
    celsius = 30
    result = convertTemperature(celsius)
    
    # Print the converted temperatures
    print(f"{celsius}°C is equal to {result[0]}°F and {result[1]}K")

if __name__ == "__main__":
    main()