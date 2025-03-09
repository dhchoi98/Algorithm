def solution(s):
    answer = [0] * 2
    """
    이진 변환의 반복, 
    각각 1의 개수 -> 제거후 길이 
    0의 개수 -> 제거한 0의 개수
    
    """    
    while s != "1":
        answer[1] += s.count("0") # 제거할 0의 개수
        after_length = s.count("1") # 0 제거 후 길이
        s = format(after_length, 'b') # 이진 변환 결과
        answer[0] += 1
    

    return answer