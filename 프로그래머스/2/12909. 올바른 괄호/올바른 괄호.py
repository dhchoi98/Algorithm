def solution(s):
    answer = True
    
    pattern = { ")" : "("}
    stack = []
    
    for c in s:
        if c == "(":   # 왼쪽 괄호
            stack.append(c)
        elif not stack or pattern[c] != stack.pop():
            return False
        
    return len(stack) == 0
