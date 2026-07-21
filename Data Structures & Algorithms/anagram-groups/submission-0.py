class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = {}
        #go through each string, sort the string(a comes before z)
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in anas:
                anas[ss].append(s) #i don't think this will work, likely need update
            else:
                anas[ss] = [s]
        return list(anas.values())
        #if that key exists in the anas map then add it to the value array
        #else, add it to the map

        #return the values of the map