import sys

N = int(sys.stdin.readline())
mylist = []


for i in range(N):
    n = int(sys.stdin.readline())
    mylist.append(n)


mylist.sort()
for i in range(N):
    print(mylist[i])