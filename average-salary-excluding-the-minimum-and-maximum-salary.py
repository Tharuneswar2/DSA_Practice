# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def average(salary):
    # Calculate the total sum of all salaries
    total_sum = sum(salary)
    
    # Remove the minimum and maximum salaries from the total sum
    total_sum -= min(salary) + max(salary)
    
    # Calculate the average salary excluding the minimum and maximum salaries
    # We subtract 2 from the total count of salaries because we excluded the minimum and maximum salaries
    average_salary = total_sum / (len(salary) - 2)
    
    return average_salary