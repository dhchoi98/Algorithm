import sys

N = int(sys.stdin.readline())

points = [[0, 0] for _ in range(N)]

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points[i] = [x, y]

sorted_points = sorted(points, key=lambda x: (x[1], x[0]))

for j in range(N):
    print(sorted_points[j][0], sorted_points[j][1])

