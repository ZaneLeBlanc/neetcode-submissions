class Solution:
    def isValid(self, s: str) -> bool:
        sta = []
        for c in s:
            if c in ('(', '[', '{'):
                sta.append(c)
            else:
                if len(sta) == 0:
                    return False
                match(c):
                    case ')':
                        if sta.pop() != '(':
                            return False
                    case ']':
                        if sta.pop() != '[':
                            return False
                    case '}':
                        if sta.pop() != '{':
                            return False
        if len(sta) != 0:
            print(sta)
            return False
        return True