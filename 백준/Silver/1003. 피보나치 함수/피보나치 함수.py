import sys
"""
아이디어 :
n의 0과 1 출력 횟수는 n - 1 과 n - 2의 0과 1 출력 횟수 합


"""



N = int(sys.stdin.readline().strip())


dp_zero = [0] * (41)
dp_one = [0] * (41)
dp_zero[0] = 1
dp_one[0] = 0

dp_zero[1] = 0
dp_one[1] = 1

for i in range(N):
    testcase = int(sys.stdin.readline().strip())
    for j in range(2, testcase + 1):
        dp_zero[j] = dp_zero[j - 1] + dp_zero[j - 2]
        dp_one[j] = dp_one[j - 1] + dp_one[j - 2]
    print(dp_zero[testcase], dp_one[testcase])