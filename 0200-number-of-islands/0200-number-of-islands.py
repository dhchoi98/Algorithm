class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0]) # 가로, 세로
        islands = 0
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(sr: int, sc: int) -> None:
            q = deque()
            q.append((sr, sc))      
            grid[sr][sc] = '0' # 방문 처리 (재방문 방지)

            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)
        
        return islands
        

