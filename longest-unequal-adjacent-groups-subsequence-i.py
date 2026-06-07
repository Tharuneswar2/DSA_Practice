def longestUnequalGroupsSubsequenceI(nums):
    # Initialize variables to store the longest subsequence and the current subsequence
    longest_subseq = 0
    current_subseq = 1
    
    # Iterate over the list of numbers
    for i in range(1, len(nums)):
        # If the current number is not equal to the previous number, 
        # it means we can extend the current subsequence
        if nums[i] != nums[i - 1]:
            current_subseq += 1
        # If the current number is equal to the previous number, 
        # it means we need to start a new subsequence
        else:
            # Update the longest subsequence if the current subsequence is longer
            longest_subseq = max(longest_subseq, current_subseq)
            current_subseq = 1
    
    # Update the longest subsequence one last time
    longest_subseq = max(longest_subseq, current_subseq)
    
    return longest_subseq