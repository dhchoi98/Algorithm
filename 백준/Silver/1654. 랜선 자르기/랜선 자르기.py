import sys

# 가지고 있는 랜선의 개수 K, 필요한 랜선의 개수 N
K, N = map(int, sys.stdin.readline().split())

# 랜선들의 길이
LAN = [int(sys.stdin.readline()) for _ in range(K)]

left, right = 1, max(LAN) # 탐색 구간
ans = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for x in LAN:
        cnt += x // mid # mid 길이로 몇 개 나오는지

    if cnt >= N:        # N개 이상 만들 수 있으면 더 길게 시도
        ans = mid       # mid는 유효 후보
        left = mid + 1
    else:               # 부족하면 길이를 줄임
        right = mid - 1

print(ans)