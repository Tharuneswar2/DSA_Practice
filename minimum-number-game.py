def minNumberGame(nums):
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    def get_sum(left, right):
        return prefix_sum[right + 1] - prefix_sum[left]

    memo = {}

    def dp(left, right):
        if left >= right:
            return 0
        if (left, right) in memo:
            return memo[(left, right)]

        # try to find the minimum difference by splitting the array into two parts
        res = float('inf')
        for i in range(left, right):
            # calculate the difference between the sum of the left part and the sum of the right part
            diff = abs(get_sum(left, i) - get_sum(i + 1, right))
            # recursively find the minimum difference for the left and right parts
            res = min(res, max(dp(left, i), dp(i + 1, right), diff))

        memo[(left, right)] = res
        return res

    return dp(0, n - 1)