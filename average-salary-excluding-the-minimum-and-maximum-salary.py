def average(salary):
    # Calculate the total sum of salaries
    total_sum = sum(salary)
    
    # Remove the minimum and maximum salaries from the total sum
    total_sum -= min(salary) + max(salary)
    
    # Calculate the average salary excluding the minimum and maximum salaries
    # We subtract 2 from the total count of salaries because we removed two salaries
    average_salary = total_sum / (len(salary) - 2)
    
    return average_salary

# Example usage:
salary = [4000, 3000, 1000, 2000]
print(average(salary))