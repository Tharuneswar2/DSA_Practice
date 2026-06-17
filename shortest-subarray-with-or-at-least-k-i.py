from collections import deque

def shortestSubarray(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] | nums[i]

    res = n + 1
    dq = deque()
    for i in range(n + 1):
        while dq and prefix[i] <= prefix[dq[0]]:
            dq.popleft()
        while dq and prefix[i] - prefix[dq[-1]] >= k:
            res = min(res, i - dq.pop())
        dq.append(i)

    return res if res <= n else -1