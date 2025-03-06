def solution(answers):
    score = [0] * 3
    num_of_answers = len(answers)
    result = []
    
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(num_of_answers):
        ans = answers[i]
        if(student1[i%len(student1)] == ans):
            score[0] += 1
        if(student2[i%len(student2)] == ans):
            score[1] += 1
        if(student3[i%len(student3)] == ans):
            score[2] += 1 
    
    for idx, s in enumerate(score):
    	if s == max(score):
        	result.append(idx+1)
    
    
    return result