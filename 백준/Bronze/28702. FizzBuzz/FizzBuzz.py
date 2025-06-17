import sys

arr = [sys.stdin.readline().strip() for _ in range(3)]
num = None
for i in range(3):
    if arr[i].isdigit():
        num = int(arr[i]) + (3 - i)
        break

if num % 15 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)