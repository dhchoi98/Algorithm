def solution(n, computers):
    
    # 아이디어 : 첫번째 컴퓨터부터 순차적으로 DFS
    
    visited = [False] * n
    
    def dfs(vertex: list):
        for index, val in enumerate(vertex):
            if val == 1 and visited[index] == False:
                visited[index] = True # 방문
                dfs(computers[index])
                 
    answer = 0
    
    for index, vertex in enumerate(computers):
        if 1 in vertex and visited[index] == False:
            answer +=1
            dfs(vertex)
        
    return answer