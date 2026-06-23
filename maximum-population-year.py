def maximumPopulation(logs):
    # Initialize a list to store the population change at each year
    population_change = [0] * 1001
    
    # Iterate over each log
    for birth, death in logs:
        # For each log, increment the population at the birth year and decrement at the death year
        population_change[birth - 1950] += 1
        population_change[death - 1950] -= 1
    
    # Initialize variables to keep track of the maximum population and the year it occurs
    max_population = 0
    max_population_year = 0
    current_population = 0
    
    # Iterate over the population change list
    for year, change in enumerate(population_change):
        # Update the current population
        current_population += change
        
        # If the current population is greater than the max population, update the max population and year
        if current_population > max_population:
            max_population = current_population
            max_population_year = year + 1950
    
    # Return the year with the maximum population
    return max_population_year