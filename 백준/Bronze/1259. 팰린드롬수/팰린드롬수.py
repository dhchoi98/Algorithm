import sys

while(True):
    num = sys.stdin.readline().strip()
    if int(num) == 0:
        break
    elif len(num) % 2 == 0: # 짝수
        mid = len(num) // 2
        left = num[:mid]
        right = num[mid:]
        right = right[::-1]
    else: # 홀수
        mid = len(num) // 2
        left = num[:mid]
        right = num[mid + 1:]
        right = right[::-1]

    if left == right:
        print("yes")
    else:
        print("no")
