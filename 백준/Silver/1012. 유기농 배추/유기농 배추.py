import sys
from collections import deque

T = int(sys.stdin.readline())


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))


for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    field = [[0 for col in range(M)] for row in range(N)]
    visited = [[0 for col in range(M)] for row in range(N )]

    for i in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        field[Y][X] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                bfs(i, j)

    print(cnt)
