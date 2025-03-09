def solution(n):
    answer = 0
    
    binary_n = format(n, 'b')
    answer = n
    
    while True:
        answer += 1
        binary_answer = format(answer, 'b')
        
        if binary_n.count('1') == binary_answer.count('1'):
            return answer
        
    