class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            # if nums.count(n) == 1:
            #     return n
            result = result ^ n
        return result