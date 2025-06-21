import sys

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline()) # 층
    n = int(sys.stdin.readline()) # 호
    dp = [[0] * (n+1) for _ in range(k+1)]
    
    for i in range(n+1):
        dp[0][i] = i
    
    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j - 1] + dp[i- 1][j]
    
    print(dp[k][n])

