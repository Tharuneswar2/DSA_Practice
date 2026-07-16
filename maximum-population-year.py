# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maximumPopulation(logs):
    # Initialize a list to store the population change for each year
    population_change = [0] * 1001
    
    # Iterate over each log
    for birth, death in logs:
        # For each log, increment the population change at the birth year
        population_change[birth - 1950] += 1
        # Decrement the population change at the death year
        population_change[death - 1950] -= 1
    
    # Initialize variables to keep track of the maximum population and the year it occurs
    max_population = 0
    max_population_year = 0
    # Initialize the current population
    current_population = 0
    
    # Iterate over each year
    for year in range(1950, 2051):
        # Update the current population
        current_population += population_change[year - 1950]
        # If the current population is greater than the max population, update the max population and year
        if current_population > max_population:
            max_population = current_population
            max_population_year = year
    
    # Return the year with the maximum population
    return max_population_year