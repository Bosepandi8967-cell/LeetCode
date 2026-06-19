from collections import deque
class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0] * (n + 1)
        for i in range(n):
            s[i + 1] = s[i] + nums[i]
            
        dp = [0] * (n + 1)
        last_sum = [0] * (n + 1)
        
        q = deque([0])
        
        for i in range(1, n + 1):
            while len(q) > 1 and s[i] >= s[q[1]] + last_sum[q[1]]:
                q.popleft()
                
            j = q[0]
            dp[i] = dp[j] + 1
            last_sum[i] = s[i] - s[j]

            while q and (s[i] + last_sum[i] <= s[q[-1]] + last_sum[q[-1]]):
                q.pop()
                
            q.append(i)
            
        return dp[n]