import sys

N = int(sys.stdin.readline())
ropes = []

for _ in range(N):
    ropes.append(int(sys.stdin.readline()))

ropes.sort(reverse=True) # 내림차순

ans = 0
for i, w in enumerate(ropes):
    ans = max(ans, w * (i + 1))

print(ans)