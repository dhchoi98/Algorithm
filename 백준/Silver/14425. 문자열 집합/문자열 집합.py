import sys

d = {}     
count = 0   
n, m = map(int, sys.stdin.readline().split()) 

for _ in range(n):
    data = sys.stdin.readline().rstrip()
    d[data] = True  # 딕셔너리에 문자열을 key로 저장

for _ in range(m):
    data = sys.stdin.readline().rstrip()
    if data in d:   # S 집합에 존재하면
        count += 1  # 카운트 증가

print(count)