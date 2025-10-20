import sys
sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(i: int, j: int, cabbage_field: list[list[int]]):
    cabbage_field[i][j] = 0
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < len(cabbage_field) and 0 <= ny < len(cabbage_field[0]) \
           and cabbage_field[nx][ny] == 1:
            dfs(nx, ny, cabbage_field)

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())  # M: 가로(열), N: 세로(행)
    cabbage_field = [[0] * M for _ in range(N)]       # [행][열] = [N][M]

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split()) # X: 열, Y: 행
        cabbage_field[Y][X] = 1                       # [행][열]

    answer = 0
    for i in range(N):          # 행
        for j in range(M):      # 열
            if cabbage_field[i][j] == 1:
                answer += 1
                dfs(i, j, cabbage_field)

    print(answer)