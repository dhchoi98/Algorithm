from collections import deque

def solution(maps):
    answer = 0
    #[1,0,1,1,1],
    #[1,0,1,0,1],
    #[1,0,1,1,1],
    #[1,1,1,0,1],
    #[0,0,0,0,1]
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append((0,0)) # 시작지점
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵 안에서만 이동
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue

            # 벽이면 무시
            if maps[nx][ny] == 0: continue
            
            if maps[nx][ny] == 1: # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx,ny))
    
    answer = maps[len(maps) - 1][len(maps[0]) - 1]
    
    return -1 if answer == 1 else answer 