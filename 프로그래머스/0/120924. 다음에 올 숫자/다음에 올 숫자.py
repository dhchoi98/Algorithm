def solution(common):
    answer = 0
    if 2 * common[1] == common[0] + common[2]: # 등차수열
        answer = common[-1] + (common[1] - common[0])
    else:
        answer = common[-1] * (common[1] // common[0])
    return answer