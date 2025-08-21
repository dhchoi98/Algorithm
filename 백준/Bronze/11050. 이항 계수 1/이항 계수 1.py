import sys

def fact(x):
    r = 1
    for i in range(2, x + 1):
        r *= i
    return r

n, k = map(int, sys.stdin.readline().split())
print(fact(n) // (fact(k) * fact(n - k)))
