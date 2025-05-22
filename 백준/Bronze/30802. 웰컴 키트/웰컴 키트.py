import sys

N = int(sys.stdin.readline().strip())
size = list(map(int, sys.stdin.readline().strip().split()))
T, P = map(int, sys.stdin.readline().strip().split())


tShirts = 0
# 티셔츠를 T장씩 최소 몇 묶음 주문해야 하는지
for n in size:
    if n == 0:
        continue
    elif n <= T:
        tShirts += 1
    else:
        if n % T == 0:
            tShirts += n // T
        else:
            tShirts += (n // T) + 1

# 펜을 P자루씩 최대 몇 묶음 주문할 수 있는지
penQuotient = N // P
penRemainder = N % P
print(tShirts)
print(penQuotient, penRemainder)


