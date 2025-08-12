import sys

N = sys.stdin.readline().strip()
num = list(map(int, sys.stdin.readline().split()))

num.sort(reverse=True)

n = num[0]
for i in range(int(N)):
    num[i] = num[i] / n * 100

average = sum(num) / int(N)
print(average)