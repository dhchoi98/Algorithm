import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().strip().split()))

cards.sort()

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

result = []
for target in targets:
    left = lower_bound(cards, target)
    right = upper_bound(cards, target)
    result.append(str(right - left))

print(' '.join(result))