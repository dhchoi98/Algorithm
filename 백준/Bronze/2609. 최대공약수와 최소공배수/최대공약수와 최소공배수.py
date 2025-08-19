import sys


num = list(map(int, sys.stdin.readline().strip().split()))
num.sort()

a, b = num
while b != 0:
    a, b = b, a % b
gcd = a

lcm = (num[0] * num[1]) // gcd


print(gcd)
print(lcm)