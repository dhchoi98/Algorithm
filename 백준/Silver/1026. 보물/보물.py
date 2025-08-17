import sys

n = sys.stdin.readline()

a = [int(x) for x in sys.stdin.readline().split()]
b = [int(y) for y in sys.stdin.readline().split()]


a.sort()
b.sort(reverse=True)

minimum = 0
for index, value in enumerate(a):
    minimum = minimum + (value * b[index])

print(minimum)