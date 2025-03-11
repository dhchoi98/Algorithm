import sys

no_see = set()
no_heard = set()

N, M = map(int, sys.stdin.readline().strip().split())


for _ in range(N):
    temp = sys.stdin.readline().strip()
    no_see.add(temp)


for _ in range(M):
    temp = sys.stdin.readline().strip()
    no_heard.add(temp)

intersection_set = sorted(no_heard & no_see)

print(len(intersection_set))

for elem in intersection_set:
    print(elem)