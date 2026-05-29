def distMoney(candies, num_people):
    # Calculate the total number of rounds
    rounds = candies // num_people
    
    # Calculate the remaining candies
    remaining = candies % num_people
    
    # Initialize the result array with the base amount each person gets
    result = [rounds] * num_people
    
    # Distribute the remaining candies
    for i in range(remaining):
        result[i] += 1
    
    return result

def distMoneyOptimized(candies, num_people):
    # Calculate the total number of rounds
    rounds = candies // num_people
    
    # Calculate the remaining candies
    remaining = candies % num_people
    
    # Initialize the result array with the base amount each person gets
    result = [rounds] * num_people
    
    # Distribute the remaining candies
    for i in range(remaining):
        result[i] += 1
    
    # If the number of people is less than or equal to the remaining candies, 
    # we can directly return the result
    if num_people <= remaining:
        return result
    
    # Otherwise, we need to distribute the remaining candies in a circular manner
    else:
        i = 0
        while remaining > 0:
            if result[i] < rounds + 1:
                result[i] += 1
                remaining -= 1
            i = (i + 1) % num_people
    
    return result