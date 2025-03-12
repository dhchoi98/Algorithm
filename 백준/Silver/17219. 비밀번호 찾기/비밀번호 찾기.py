import sys

N, M = map(int, sys.stdin.readline().strip().split())

password_dict = {}

for _ in range(N):
    site, password = sys.stdin.readline().strip().split()
    password_dict[site] = password  # 딕셔너리에 저장
for _ in range(M):
    site = sys.stdin.readline().strip()
    if site in password_dict:
        print(password_dict[site])
