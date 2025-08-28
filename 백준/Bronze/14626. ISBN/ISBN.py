import sys

s = sys.stdin.readline().strip()  # 13글자, 그중 하나는 '*'
idx = s.index('*')

# 가중치: 인덱스가 짝수이면 1, 홀수이면 3 (ISBN-13 규칙)
def w(i):
    return 1 if i % 2 == 0 else 3

base = 0
for i, ch in enumerate(s):
    if ch == '*':
        continue
    base += w(i) * int(ch)

# 후보 0~9 중에서 전체 합이 10의 배수가 되는 값 찾기
for d in range(10):
    total = base + w(idx) * d
    if total % 10 == 0:
        print(d)
        break