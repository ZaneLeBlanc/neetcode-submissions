class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret = ret + s + 'PENIS'
        return ret
    def decode(self, s: str) -> List[str]:
        out = []
        while len(s) > 0:
            delim = s.find("PENIS")
            substr = s[0:delim]
            out.append(substr)
            s = s[delim + 5:]
        return out

