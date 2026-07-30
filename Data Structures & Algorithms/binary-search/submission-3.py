class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #0 case
        if len(nums) == 0:
            return -1
        #1 case
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
    
        a, b = 0, len(nums) -1
        while b - a > 1:
            mid = (a + b) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                b = mid - 1
            elif nums[mid] < target:
                a = mid + 1
        
        if nums[a] == target:
            return a
        elif nums[b] == target:
            return b
        else:
            return -1

        

        