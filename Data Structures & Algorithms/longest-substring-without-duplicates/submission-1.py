class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        chars = {}

        if len(s) < 2:
            return len(s)

        chars[s[l]] = 1
        #make a sliding window, once right hits a character that has been seen already
        #, move up left until it hits that char
        while r < len(s) - 1:
            
            r += 1
            if s[r] in chars:
                while True:
                    print('checking : ' + s[l])
                    
                    
                    
                    
                    if s[l] is s[r]:
                        print('sl == sr')
                        l += 1
                        break
                    chars.pop(s[l])
                    l += 1
            else:
                chars[s[r]] = 1
            longest = max(longest, r-l + 1)

        return longest
