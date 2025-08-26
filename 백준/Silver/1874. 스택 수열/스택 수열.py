import sys

n = int(sys.stdin.readline())

sequence = []

for _ in range(n):
    sequence.append(int(sys.stdin.readline()))

num = 1
stack = []
ops = []


for x in sequence:
    while num <= x:
        stack.append(num)
        ops.append('+')
        num += 1
# 이제 top이 x여야 pop 가능
    if stack and stack[-1] == x:
        stack.pop()
        ops.append('-')
    else:
        print("NO")
        sys.exit(0)

print('\n'.join(ops))