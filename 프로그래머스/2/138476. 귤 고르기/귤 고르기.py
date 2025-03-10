from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    # 귤 크기별 개수 계산
    counts = Counter(tangerine)
    
    # 개수가 많은 순서대로 정렬
    sorted_counts = sorted(counts.values(), reverse=True)
    
    # k개를 채울 때 까지 귤 종류 최소화
    total = 0
    num_types = 0
    
    for num in sorted_counts:
        total += num
        num_types += 1
        if total >= k:
            return num_types
    