def solution(brown, yellow):
    
    """
    아이디어  :  갈색 격자의 수 : 2x + 2y + 4 
              노란색 격자의 수 : xy
    
    """
    answer = []
    yellow_x = 0
    yellow_y = 0
    
    for i in range(1, yellow + 1):
        if yellow % i == 0 : # 노란색의 개수가 i로 나누어 떨어지면
            yellow_x = int(yellow/i) # 노란색의 가로는 i로 나누어 떨어진 몫
            yellow_y = i
            if yellow_x * 2 + yellow_y * 2 + 4 == brown:
                answer.append(yellow_x + 2)
                answer.append(yellow_y + 2)
                
                return sorted(answer, reverse = True) # 가로가 세로보다 크거나 같아야 하므로 내림차순 정렬
    
    return answer