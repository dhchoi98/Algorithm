def solution(progresses, speeds):
    answer = []
    stack = []
    # 반복문 한 번당 하루 지남
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            # 작업 진행
            progresses[i] += speeds[i]
        
        # 스택에 먼저 들어가있는 기능이 완료가 되어야 그 뒤 기능의 배포가 가능
        for j in range(len(progresses)):
            if progresses[0] > 99:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
        
        if cnt > 0:
            answer.append(cnt)
        
    
    
    # 앞에 있는 기능 완료되면 pop 해주기
    
    return answer