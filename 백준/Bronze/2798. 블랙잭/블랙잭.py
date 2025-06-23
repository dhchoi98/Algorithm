import sys

N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0

# 모든 가능한 3장의 카드 조합을 확인
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            current_sum = cards[i] + cards[j] + cards[k]
            
            # M을 넘지 않으면서 가장 큰 값 찾기
            if current_sum <= M and current_sum > max_sum:
                max_sum = current_sum

print(max_sum)




