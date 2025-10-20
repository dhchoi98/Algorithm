import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 8방향(상하좌우 + 대각선)
DIRS = [(-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)]

def dfs(r, c, grid, h, w):
    grid[r][c] = 0  # 방문 처리
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 1:
            dfs(nr, nc, grid, h, w)

def solve():
    out = []
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break

        grid = [list(map(int, input().split())) for _ in range(h)]

        islands = 0
        for r in range(h):
            for c in range(w):
                if grid[r][c] == 1:
                    islands += 1
                    dfs(r, c, grid, h, w)
        out.append(str(islands))

    print("\n".join(out))

if __name__ == "__main__":
    solve()
