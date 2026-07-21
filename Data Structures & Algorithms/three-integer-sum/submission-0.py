class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the list
        newNums = sorted(nums)
        res = []

        #instead of x + y + z = 0, we do: (y + z = -x)

        #for each element, set it as the (-x) by negating it *(-1)
        for i in range(len(newNums) - 1):
            goal = newNums[i] * -1
            arr = newNums.copy()
            arr.pop(i)

            l,r = 0, len(arr)-1
            while l<r:
                if arr[l] + arr[r] > goal:
                    r -= 1
                elif arr[l] + arr[r] < goal:
                    l += 1
                else:
                    #solution found
                    sol = [arr[l], arr[r], -1 * goal]
                    sol = sorted(sol)
                    if sol not in res:
                        res.append(sol)
                    l += 1
        return res
        #then do a 2 ptr setup solve, if there is a solution, sort it, and see if it exists already
        #, if it doesn't exist already, add it