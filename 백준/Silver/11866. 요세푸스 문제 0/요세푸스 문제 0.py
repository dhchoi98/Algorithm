import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())

yoseputh = deque()
result = []
for i in range(N):
    yoseputh.append(i + 1)

    death = K - 1
for _ in range(N):
    death %= len(yoseputh)  # 핵심 수정!
    result.append(yoseputh[death])
    del yoseputh[death]
    death += K - 1

print("<" + ", ".join(map(str, result)) + ">")