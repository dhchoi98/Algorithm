import sys
from collections import deque

"""

"""



N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

adj = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    adj[start].append(end)
    adj[end].append(start)

for i in range(1, N + 1):
    adj[i].sort()

visited = [False] * (N + 1)

# bfs
answer = 0
q = deque()
q.append(1)
visited[1] = True
while q:
    cur = q.popleft()
    for nxt in adj[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)
            answer += 1

print(answer)
