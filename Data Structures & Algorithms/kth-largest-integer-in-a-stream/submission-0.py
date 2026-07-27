import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify_max(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        temp_list = heapq.nlargest(self.k, self.nums)
        return temp_list[self.k-1]
