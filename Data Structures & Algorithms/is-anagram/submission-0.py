class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for each value in s, add it to a hashmap. increment value
        if len(s) != len(t):
            return False


        myDict = {}
        for char in s:
            myDict[char] = myDict.get(char, 0) + 1

        # for each value in t, add it to a hashmap, decrement value, remove when 0. 
        for char in t:
            if char not in myDict:
                return False
            myDict[char] -= 1
            if myDict[char] < 0:
                return False

        return True