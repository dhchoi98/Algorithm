import sys

while True:
    s = sys.stdin.readline().rstrip("\n")
    if s == ".":
        break

    stack = []
    balanced = True  

    for ch in s:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                balanced = False
                break
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                balanced = False
                break

    if balanced and not stack:
        print("yes")
    else:
        print("no")
