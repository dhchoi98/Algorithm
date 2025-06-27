import sys
from collections import deque

N = int(sys.stdin.readline())
stack = deque()

for i in range(N):
    stack.append(i + 1)

while len(stack) > 1:
    stack.popleft()
    stack.append(stack.popleft())


print(stack.pop())