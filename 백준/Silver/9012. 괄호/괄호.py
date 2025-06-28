import sys
from collections import deque

N = int(sys.stdin.readline())

for i in range(N):
    vps = list(sys.stdin.readline().strip())
    stack = deque()
    is_valid = True
    
    for v in vps:
        if v == '(':
            stack.append(v)
        elif v == ')':
            if stack:
                stack.pop()
            else:
                is_valid = False
                break
    
    # 스택이 비어있고 유효한 경우에만 YES
    if is_valid and not stack:
        print("YES")
    else:
        print("NO")