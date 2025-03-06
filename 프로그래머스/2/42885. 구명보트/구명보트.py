def solution(people, limit):
    people.sort()  # 몸무게를 정렬
    left, right = 0, len(people) - 1
    answer = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:  # 두 사람이 같이 탈 수 있으면
            left += 1  # 가벼운 사람 이동
        # 무거운 사람은 항상 태우고 보트 개수 증가
        right -= 1
        answer += 1  # 보트 하나 추가
    
    return answer
