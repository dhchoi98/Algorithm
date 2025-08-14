import math
import sys


n = int(sys.stdin.readline().strip())
numbers = []
if n == 0:
    print(0)
    sys.exit(0)
    
for i in range(n):
    numbers.append(int(sys.stdin.readline().strip()))

trimmed = math.floor(n * 0.15 + 0.5)

numbers.sort()
numbers = numbers[trimmed: n - trimmed]

average = math.floor(sum(numbers) / len(numbers) + 0.5)

print(average)