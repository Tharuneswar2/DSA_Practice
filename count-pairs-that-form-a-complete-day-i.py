def count_pairs(years):
    # Create a dictionary to store the frequency of each year
    freq = {}
    
    # Initialize count of pairs to 0
    count = 0
    
    # Iterate over each year in the list
    for year in years:
        # Calculate the complement year
        complement = 2023 - year
        
        # If the complement year is already in the dictionary, increment the count
        if complement in freq:
            count += freq[complement]
        
        # Increment the frequency of the current year
        freq[year] = freq.get(year, 0) + 1
    
    # Return the total count of pairs
    return count

# Test the function
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
print(count_pairs(years))