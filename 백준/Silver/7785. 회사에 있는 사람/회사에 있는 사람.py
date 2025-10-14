import sys


n = int(sys.stdin.readline())
d = set()

for _ in range(n):
    name, state = sys.stdin.readline().split()
    if state == "enter":
        d.add(name)
    else:
        d.remove(name)

for name in sorted(d, reverse=True):  # 사전 역순 정렬
    print(name)