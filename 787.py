# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 03:28:01 2021

"""

from collections import defaultdict
import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append((v, w))
            
        Q = [(0, src, K)]
        while Q:
            cost, node, k = heapq.heappop(Q)
            if node == dst:
                return cost
            if k >= 0:
                for v, w in graph[node]:
                    alt = cost + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1

n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
ret = Solution()
print(ret.findCheapestPrice(n, edges, src, dst, k))

"""
743번 문제와 비슷한 유형이여서 어느 정도 까지는 코드를 짜보고 부족한 부분을 고쳐가며 문제를 해결하였다.
딕셔너리에 key를 출발지로, value에 도착지와 비용을 넣어두고 다음 도착지로 갈 때 마다 꺼내서 업데이트 하는 방법으로 문제를 해결하였다.
이동 가능 횟수인 k가 남아있을 경우, 다음 큐에 추가할 때 k-1만큼을 해주어서 추가한다.
다른 풀이로는 딕셔너리가 아닌 2차원 배열을 이용하여 푸는 방법도 있으며, 시간은 비슷하게 걸린다.
"""
