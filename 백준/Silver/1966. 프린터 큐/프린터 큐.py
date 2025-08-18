import sys
from collections import deque
from operator import itemgetter

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))

    q = deque((i, p) for i, p in enumerate(priorities))
    printed = 0

    while True:
            max_val = max(map(itemgetter(1), q))

            i, p = q[0]
            if p == max_val:
                q.popleft()
                printed += 1
                if i == m:
                    print(printed)
                    break
            else:
                q.rotate(-1)