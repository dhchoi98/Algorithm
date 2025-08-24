import sys

L = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
H = 0
for index, c in enumerate(s):
    a = ord(c) - ord('a') + 1
    r = 31 ** index
    H = H + a * r

H = H % 1234567891

print(H)