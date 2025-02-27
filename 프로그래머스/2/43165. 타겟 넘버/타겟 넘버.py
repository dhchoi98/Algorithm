def solution(numbers, target):
    answer = 0

    def dfs(index, total):
        nonlocal answer
        if index == len(numbers):  # 모든 숫자를 사용했을 때
            if total == target:
                answer += 1
            return
        
        # 현재 숫자를 더하는 경우
        dfs(index + 1, total + numbers[index])
        # 현재 숫자를 빼는 경우
        dfs(index + 1, total - numbers[index])

    dfs(0, 0)  # 초기 호출
    return answer
