class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #foreach nums, remove the num, and try and remove again
        for n in nums:
            if nums.count(n) == 1:
                return n
        #if none is returned, that's the special number
        #else, remove that as well