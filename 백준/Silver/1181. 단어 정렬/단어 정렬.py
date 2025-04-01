import sys

N = int(sys.stdin.readline())
words = set()  # 중복 제거를 위해 set 사용

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    words.add(word)  # set은 중복된 단어는 자동으로 무시함

# set은 순서가 없기 때문에, 정렬된 리스트로 다시 변환
sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)