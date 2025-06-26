import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
mArr = list(map(int, sys.stdin.readline().split()))

A.sort()

for i in mArr:
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == i:
            print(1)
            break
        elif A[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    else:
        print(0)