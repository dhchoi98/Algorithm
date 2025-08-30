import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)

def bfs(start: int):
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

components = 0
for node in range(1, N + 1):
    if not visited[node]:
        bfs(node)
        components += 1

print(components)
