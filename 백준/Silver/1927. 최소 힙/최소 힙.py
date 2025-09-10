import sys
import heapq

min_heap = []

# 연산의 개수 N
N = int(sys.stdin.readline())

for i in range(N):
    #  연산에 대한 정보를 나타내는 정수 x
    x = int(sys.stdin.readline())
    # x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산
    if x != 0:
        heapq.heappush(min_heap, x)

    else:
        # 0이 주어진 횟수만큼 답을 출력한다.
        # 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.
        if not min_heap:
            print(0)
        # x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우
        else:
            print(heapq.heappop(min_heap))