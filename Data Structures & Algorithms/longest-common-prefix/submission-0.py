class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""

        else:
            strs.sort()

            fir = strs[0]
            last = strs[-1]

            i = 0

            while i<len(fir) and i<len(last) and fir[i]==last[i]:
                i = i+1
            
            return fir[0:i]