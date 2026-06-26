class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s 
        return res
    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        while i < len(s):
            j=i
            while s[j] != "#":
                j = j +1
            len_str = int(s[i:j])
            string = s[j+1:j+1+len_str]
            dec.append(string)
            i = len_str + j + 1
        return dec