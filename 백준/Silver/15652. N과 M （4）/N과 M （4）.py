
"""
입력 :  1부터 n 까지의 자연수를 나타내는 n, n개 중 m개를 선택    
"""
def backtrack(n, m, seq):
    if len(seq) == m: # m개 선택 완료시에 DFS 종료
        print(*seq)
        return
    start = seq[-1] if seq else 1
    for i in range(start, n + 1):
        backtrack(n, m, seq + [i])


n, m = map(int, input().split())

backtrack(n, m,[])
