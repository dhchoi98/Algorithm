import sys


white, blue = 0, 0

# 입력 :
# 전체 종이의 한 변의 길이 N , N은 2, 4, 8, 16, 32, 64, 128 중 하나
N = int(sys.stdin.readline())

# 색종이의 각 가로줄의 정사각형칸들의 색
color_paper = [list(map(int ,sys.stdin.readline().split())) for _ in range(N)]

def count_colors(x: int, y: int, size: int):
    """
    (x, y)에서 시작하는 size x size 정사각형 내
    (white_count, blue_count)를 반환
    """
    first = color_paper[x][y]

    # 같은 색인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if color_paper[i][j] != first:
                # 색이 섞여 있으면 4등분
                half = size // 2
                count_colors(x, y, half) # 좌상
                count_colors(x, y + half, half) # 우상
                count_colors(x + half, y, half) # 좌하
                count_colors(x + half, y + half, half) # 우하
                return

    global white, blue
    # 전부 같은색이면 for문 빠져나옴 -> 색종이 카운트
    if first == 0:
        white += 1
    else:
        blue += 1


count_colors(0, 0, N)

# 출력 :
# 첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고
print(white)

# 둘째 줄에는 파란색 색종이의 개수를 출력
print(blue)