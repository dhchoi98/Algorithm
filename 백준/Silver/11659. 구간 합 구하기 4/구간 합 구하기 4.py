import sys


N, M = map(int, sys.stdin.readline().strip().split())

nums = list(map(int, input().split()))
pre = [0]
mysum = 0

for i in range(N):
  mysum += nums[i]
  pre.append(mysum)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(pre[j] - pre[i - 1])
