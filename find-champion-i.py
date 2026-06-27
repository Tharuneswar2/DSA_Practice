def find_champion_I(candidates, votes):
    # Create a dictionary to store the votes for each candidate
    vote_count = {}
    
    # Iterate over the votes and update the vote count for each candidate
    for vote in votes:
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1
    
    # Find the candidate with the most votes
    champion = max(vote_count, key=vote_count.get)
    
    # Return the champion
    return champion

# Example usage:
candidates = ['John', 'Mary', 'David']
votes = ['John', 'Mary', 'John', 'David', 'Mary', 'John', 'Mary', 'John']
print(find_champion_I(candidates, votes))  # Output: John