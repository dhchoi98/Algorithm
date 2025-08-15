import sys

expr = sys.stdin.readline().strip()

parts = expr.split('-')

def ssum(s: str) -> int:
    return sum(map(int, s.split('+')))

ans = ssum(parts[0])          
for p in parts[1:]:
    ans -= ssum(p)             
print(ans)