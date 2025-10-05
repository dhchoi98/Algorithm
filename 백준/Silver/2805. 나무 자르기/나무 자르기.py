import sys

# 나무의 수 N, 집으로 가져가려고 하는 나무의 길이 M

N, M = map(int, sys.stdin.readline().strip().split())

# 나무의 높이
tree_heights = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(tree_heights)

max_height = 0

while left <= right:
    mid = (left + right) // 2
    cutted_tree = 0
    for height in tree_heights:
        if mid < height:
            cutted_tree += height - mid

    if cutted_tree < M:
        right = mid - 1

    else:
        left = mid + 1
        max_height = mid

print(max_height)
