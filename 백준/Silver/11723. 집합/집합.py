import sys

N = int(sys.stdin.readline().strip())
S = set()

for _ in range(N):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:  # "all" 또는 "empty"
        if temp[0] == "all":
            S = {i for i in range(1, 21)}
        elif temp[0] == "empty":
            S.clear()
    else:
        command, x = temp[0], int(temp[1])

        if command == "add":
            S.add(x)
        elif command == "remove":
            S.discard(x)  # KeyError 방지
        elif command == "check":
            print(1 if x in S else 0)  # 즉시 출력
        elif command == "toggle":
            S.symmetric_difference_update({x})  # 빠른 토글 연산
