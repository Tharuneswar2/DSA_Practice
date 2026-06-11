def kItemsWithMaximumSum(k, prices):
    # Sort the prices in descending order to get the maximum sum
    prices.sort(reverse=True)
    
    # Initialize the sum with 0
    total_sum = 0
    
    # Iterate over the first k prices and add them to the sum
    for i in range(k):
        total_sum += prices[i]
    
    # Return the total sum
    return total_sum

# Test the function
print(kItemsWithMaximumSum(3, [1, 2, 3, 4, 5]))  # Output: 12