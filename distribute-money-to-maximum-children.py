# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def distMoney(candies, num_people):
    # Calculate the total number of rounds we can distribute candies
    rounds = candies // num_people
    
    # Calculate the remaining candies after distributing the rounds
    remaining_candies = candies % num_people
    
    # Initialize the result array with the number of people
    result = [0] * num_people
    
    # Distribute the candies for each round
    for i in range(rounds):
        # For each round, distribute candies to each person
        for j in range(num_people):
            # Add the current round number plus one to the result array
            result[j] += i + 1
    
    # Distribute the remaining candies
    for i in range(remaining_candies):
        # Add one to the result array for the remaining candies
        result[i] += rounds + 1
    
    return result