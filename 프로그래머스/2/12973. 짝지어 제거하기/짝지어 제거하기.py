def solution(s):
    answer = -1
    stack = []
    
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])  # 스택이 비어있다면 push
        else:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
    
    if len(stack) == 0:
        return 1
        
    
    return 0