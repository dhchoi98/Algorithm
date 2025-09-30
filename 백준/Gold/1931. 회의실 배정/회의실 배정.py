import sys


N = int(sys.stdin.readline())

meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 종료 시간 오름차순 -> 시작 시간 오름차순 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end = 0

# 순회하면서 조건 체크
for start, end in meetings:
    if start >= last_end:
        count += 1
        last_end = end

print(count)