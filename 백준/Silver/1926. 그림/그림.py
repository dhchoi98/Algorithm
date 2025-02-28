from collections import deque

n, m = map(int, input().split()) # 도화지의 세로, 가로 크기 
map = [list(map(int, input().split())) for _ in range(n)] # 도화지
chk = [[False] * m for _ in range(n)] # 방문 여부
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def bfs(y, x):
    q = deque()
    q.append((y,x))
    extent = 1

    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    extent += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))
                    
    return extent
                    

    

cnt = 0
max_picture = 0

for i in range(n):
    for j in range(m):
        if map[i][j] == 1 and chk[i][j] == False:
            # 전체 그림 개수 + 1, BFS를 통해 그림 넓이 계산 -> 최대값 갱신
            cnt += 1
            chk[i][j] = True
            max_picture = max(max_picture, bfs(i,j)) 
            
            
print(cnt)
print(max_picture)