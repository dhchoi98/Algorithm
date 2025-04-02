import sys

N = int(sys.stdin.readline())
cnt = 0
end_num = 666

while True:
    if '666' in str(end_num):
        cnt += 1

    end_num += 1

    if cnt == N:
        print(end_num - 1)
        break
