def generator(n):
    total = n
    x = n
    while x > 0:
        total += x % 10
        x //= 10
    return total

def find_smallest_generator(n):
    d = len(str(n))
    start = max(1, n - 9 * d)
    for m in range(start, n):
        if generator(m) == n:
            return m
    return 0

if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline().strip())
    print(find_smallest_generator(n))