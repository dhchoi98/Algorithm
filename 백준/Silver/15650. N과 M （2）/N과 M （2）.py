from itertools import combinations

"""
입력 :  1부터 n 까지의 자연수를 나타내는 n, n개 중 m개를 선택    
"""

n, m = map(int, input().split())
input_list = []

for i in range(1, n + 1):
    input_list.append(i)
    
perm = list(combinations(input_list, m))    

for p in perm:
    print(" ".join(map(str, p)))