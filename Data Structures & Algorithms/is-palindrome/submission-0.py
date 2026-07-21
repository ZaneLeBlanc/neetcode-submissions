class Solution:
    def isPalindrome(self, s: str) -> bool:
        #trim string
        t = self.removeNonAlphaNumChars(s.lower())

        #len = 0?
        #len = 1?
        #len = 2?
        if len(t) <= 1:
            return True

        #setup the two pointers
        ptr1 = 0
        ptr2 = len(t) - 1
        
        while ptr1 <= ptr2:
            if t[ptr1] != t[ptr2]:
                return False;
            else:
                ptr1+=1
                ptr2-=1
        return True

    def removeNonAlphaNumChars(self, s: str) -> str:
        clean_text = ''.join(filter(str.isalnum, s))
        return clean_text
        