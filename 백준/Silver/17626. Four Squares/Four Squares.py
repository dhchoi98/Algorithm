import sys

n = int(sys.stdin.readline())

# 라그랑주의 네 제곱수 정리를 활용한 최적화
# 모든 자연수는 최대 4개의 제곱수의 합으로 표현 가능

# n이 완전제곱수인지 확인
i = 1
while i * i <= n:
    if i * i == n:
        print(1)
        sys.exit()
    i += 1

# n이 두 제곱수의 합인지 확인
for i in range(1, int(n**0.5) + 1):
    j = int((n - i*i)**0.5)
    if i*i + j*j == n:
        print(2)
        sys.exit()

# n이 4^a(8b+7) 형태인지 확인 (라그랑주 정리에 의해 이 경우만 4개 필요)
while n % 4 == 0:
    n //= 4

if n % 8 == 7:
    print(4)
else:
    print(3)