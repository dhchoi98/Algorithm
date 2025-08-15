import sys
# 그리디 알고리즘

N, K = map(int, sys.stdin.readline().strip().split())

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline().strip()))
coins.sort(reverse=True)

answer = 0
for coin in coins:
    if K >= coin:
        answer += K // coin
        K %= coin
        if K <= 0:
            break
print(answer) 
