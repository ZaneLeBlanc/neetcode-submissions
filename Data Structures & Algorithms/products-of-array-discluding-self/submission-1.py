class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #calculate the total product
        prod = 1
        zerosExist = 0
        for i in nums:
            if i == 0:
                zerosExist += 1
            elif zerosExist < 2:
                prod *= i
            
            if zerosExist > 1:
                prod = 0

        output = [prod] * len(nums)
        if zerosExist > 1:
            return output

        #using this total product,
        #setup a output array, where each element is this total product

        #for each element, divide and reset it to the result
        for i in range(len(output)):
            if zerosExist == 1:
                if nums[i] == 0:
                    output[i] = prod
                else:
                    output[i] = 0
            else:
                output[i] = int(output[i] / (nums[i]))
        #return this array
        return output