from collections import deque

def dfs(c):
    ans_dfs.append(c) # 최종 경로 배열에 추가
    visited[c] = 1    # 방문 표시
   
    for n in adj[c]:
        if visited[n] == 0:
            dfs(n)

def bfs(s):
    q = deque() # 필요한 q , visited[], 변수 생성
    
    q.append(s) # Q 에 초기데이터 (들) 삽입
    ans_bfs.append(s)
    visited[s] = 1
    
    while q:
        c = q.popleft()
        for n in adj[c]:
            if visited[n] == 0:
                q.append(n)
                ans_bfs.append(n)
                visited[n] = 1

N, m, v = map(int, input().split()) # 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
adj = [[] for _ in range(N + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)
    
for i in range(N + 1):
    adj[i].sort()
    
visited = [0] * (N + 1)
ans_dfs = []
dfs(v) # 시작 정점을 매개변수로 

visited = [0] * (N + 1)
ans_bfs = []
bfs(v)

print(*ans_dfs)
print(*ans_bfs)