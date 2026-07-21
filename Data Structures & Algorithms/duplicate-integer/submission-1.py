class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = set()
        for i in nums:
            if i not in myDict:
                myDict.add(i)
            else:
                return True
        return False
