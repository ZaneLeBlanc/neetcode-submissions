class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #go through nums, put together a hashmap of characters and their occurrences
        hm = {}
        ret = []
        for i in nums:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
        #find key of hashmap the associates with value
        hmitems = list(hm.items())
        print(hmitems)
        hmitems.sort(reverse=True, key=lambda x: x[1])
        

        for i in range(k):
            ret.append(hmitems[i][0])

        return ret