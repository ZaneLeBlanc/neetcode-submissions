class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)
            res = self.calcBreak(s1, s2)
            if res != 0:
                heapq.heappush_max(stones, res)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]


    def calcBreak(self, s1: int, s2: int) -> int:
        return abs(s1 - s2)