class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #sort the list
        s = sorted(nums)

        #using two pointers, one at start one at end
        l, r = 0, len(s) - 1
        val1 = -1
        val2 = -1

        #go through and find the target adjusting pointers
        while l < r:
            total = s[l] + s[r]
            
            if total == target:
                val1 = s[l]
                val2 = s[r]
                break;
            elif total < target:
                l += 1
            else:
                r -= 1


        #when 2 values are aquired, store them,


        #find index of 1st value
        i1 = nums.index(val1)
    
        #find index of 2nd value
        offset = i1 + 1 if val1 == val2 else 0
        i2 = nums.index(val2, offset)

        #return smaller index first
        if i1 < i2:
            return [i1, i2]
        else:
            return [i2, i1]