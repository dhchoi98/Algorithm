import collections, heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # pq: (누적비용, 정점, 남은 비행 가능 횟수)  — 비행 횟수는 최대 k+1
        pq = [(0, src, k + 1)]

        # best_rem[node] = 이 정점에 도달했을 때 '가장 많이 남겨본(rem)' 값
        # rem이 작거나 같은 상태로 다시 오면 프루닝
        best_rem = [-1] * n

        while pq:
            cost, u, rem = heapq.heappop(pq)
            if u == dst:
                return cost
            if rem == 0:
                continue
            # 이미 u에 더 많은 rem으로 도달한 적이 있으면 skip
            if best_rem[u] >= rem:
                continue
            best_rem[u] = rem

            for v, w in graph[u]:
                heapq.heappush(pq, (cost + w, v, rem - 1))

        return -1
