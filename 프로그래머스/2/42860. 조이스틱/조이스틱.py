def solution(name):
    """
     아이디어 : 상, 하, 좌, 우 변수 값을 만들어놓고
     for문 돌려서 몇번 조작해야되는지 저장
     
     이때 A면 그쪽 방문하지 않아도 되므로 어떤 움직임이 최소값이 될지 계산해야함
     (오른쪽으로 가는게 가까울지 왼쪽으로 가는게 가까울지)
     
     그리디이니 왼쪽부터 순차적으로 탐색하면 될듯    
    """
    
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1
    
    answer = 0
    distance = [0] * len(name)
    
    
    for i, v in enumerate(name):
        # 알파벳 변경, 위로 이동하는게 짧을지 아래로 이동하는게 짧을지 계산해야함
        # 대문자로만 이루어져 있으므로 아스키 코드값을 통해 이동 거리 계산      
        
        # 'Z'의 아스키 코드 값 : 90  , Z로의 움직임 + 1
        # 'A'의 아스키 코드 값 : 65 
        answer += min(ord(v) - ord('A'), ord('Z') - ord(v) + 1)
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) -next)])
        
        print("i : ", i)
        print("v : ", v)
        
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer