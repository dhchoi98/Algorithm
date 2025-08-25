import sys

A, B, V = map(int, sys.stdin.readline().split())

# 예외 처리: 첫날 바로 도달 가능한 경우
if A >= V:
    print(1)
else:
    # days = ceil((V - B) / (A - B))를 정수연산으로
    days = (V - B + (A - B) - 1) // (A - B)
    print(days)
