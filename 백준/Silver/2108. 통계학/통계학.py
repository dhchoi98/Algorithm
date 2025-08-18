import sys
from collections import Counter

N = int(sys.stdin.readline().strip())

numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))


# 산술 평균 (N개의 수들의 합을 N으로 나눈 값, 소수점 이하 첫째 자리에서 반올림한 값을 출력)
average = round((sum(numbers) / len(numbers)))
print(average)

# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
numbers.sort()
mid = len(numbers) // 2
print(numbers[mid])

# 최빈값 : N개의 수들 중 가장 많이 나타나는 값

counter = Counter(numbers)

# 1. 최빈값 빈도 구하기
max_freq = max(counter.values())

# 2. 최빈값 후보 추출
modes = [num for num, cnt in counter.items() if cnt == max_freq]

# 3. 정렬 후 두 번째로 작은 값 출력
modes.sort()
if len(modes) >= 2:
    print(modes[1])  # 두 번째로 작은 값
else:
    print(modes[0])  # 최빈값이 하나뿐이면 그 값 출력


# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
range_number = numbers[-1] - numbers[0]
print(range_number)