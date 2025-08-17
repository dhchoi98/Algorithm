import sys
import math

m, n = map(int, sys.stdin.readline().strip().split())

prime_number = []

for i in range(m, n + 1):
    if i < 2:
        continue
    root_n = math.isqrt(i)
    is_prime = True
    for j in range(2, root_n + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_number.append(i)

for i in prime_number:
    print(i)
