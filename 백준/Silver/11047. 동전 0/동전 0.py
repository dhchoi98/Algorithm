import sys


# 동전의 종류, 만들어야 할 가치 합
n, k = map(int, sys.stdin.readline().split())

coins = []
# 동전의 가치 배열 coins(i)
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
coins.sort(reverse=True)

ans = 0
for coin in coins:
    if k == 0: break
    ans += k // coin
    k = k % coin


print(ans)