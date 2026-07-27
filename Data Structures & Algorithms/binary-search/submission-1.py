class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bot, top = 0, len(nums) - 1

        print('bot, top = ' + str(bot) + ', ' + str(top))
        while top - bot > 1:
            print('bot, top = ' + str(bot) + ', ' + str(top))

            mid = (int((top - bot) / 2) + bot)
            print('mid = ' + str(mid))
            if nums[mid] < target:
                bot = mid
            elif nums[mid] > target:
                top = mid
            else:
                return mid
            print('bot, top = ' + str(bot) + ', ' + str(top))

        if nums[top] == target:
            return top
        elif nums[bot] == target:
            return bot
        else:
            return -1
        