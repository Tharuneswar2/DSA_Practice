# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
class Solution:
    def totalMoney(self, n: int) -> int:
        # Initialize total money to 0
        total_money = 0
        
        # Calculate the number of full weeks
        full_weeks = n // 7
        
        # Calculate the remaining days
        remaining_days = n % 7
        
        # Calculate the total money for full weeks
        # Each week, the money increases by 1, so the total money for a week is the sum of an arithmetic sequence
        # The sum of an arithmetic sequence can be calculated as (n * (a1 + an)) / 2, where n is the number of terms, a1 is the first term, and an is the last term
        # In this case, the first term is 1 and the last term is 7, so the sum of a week is (7 * (1 + 7)) / 2 = 28
        # Since there are full_weeks weeks, the total money for full weeks is 28 * full_weeks
        total_money += 28 * full_weeks
        
        # Calculate the total money for the remaining days
        # The money for the remaining days is the sum of an arithmetic sequence with first term 1 and last term remaining_days
        # The sum of an arithmetic sequence can be calculated as (n * (a1 + an)) / 2, where n is the number of terms, a1 is the first term, and an is the last term
        # In this case, the number of terms is remaining_days, the first term is 1, and the last term is remaining_days
        # So the sum of the remaining days is (remaining_days * (1 + remaining_days)) / 2
        # However, we need to add the money for the full weeks to the first day of the remaining days, so we add full_weeks to the first term
        # So the sum of the remaining days is (remaining_days * (full_weeks + 1 + full_weeks + remaining_days)) / 2
        total_money += (remaining_days * (full_weeks + 1 + full_weeks + remaining_days)) // 2
        
        # Return the total money
        return total_money