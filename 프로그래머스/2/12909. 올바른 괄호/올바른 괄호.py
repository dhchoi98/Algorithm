def solution(s):
    stack = []
    
    for char in s:
        if char == "(": # 왼쪽 괄호면 스택에 삽입
            stack.append(char)
        elif not stack or "(" != stack.pop() : # 오른쪽 괄호라면 닫힌 괄호인지 확인
            return False # 문자열이 끝나지 않았는데 스택이 비어있다는 것은 오른쪽 괄호가 더 많다는 것
    
    return len(stack) == 0 # 다 끝났을 때 비어있다는 것은 True 인 것