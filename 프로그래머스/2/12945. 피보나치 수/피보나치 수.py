import collections

def solution(n):
    answer = 0
    dp = collections.defaultdict(int)
    
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    answer = dp[n] % 1234567
    
    
    return answer