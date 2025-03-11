import sys
# 그리디 알고리즘

N = int(sys.stdin.readline().strip())

pi_values = list(map(int, sys.stdin.readline().strip().split()))
   
# P값을 오름차순으로 정렬 (최적의 대기 순서를 만들기 위해)
pi_values.sort()

# 최소 시간의 합 계산
total_time = 0  # 전체 시간의 합
accumulated_time = 0  # 현재까지 대기한 시간

for time in pi_values:
    accumulated_time += time  # 현재 사람이 대기한 시간
    total_time += accumulated_time  # 총 대기 시간에 추가

# 결과 출력
print(total_time)