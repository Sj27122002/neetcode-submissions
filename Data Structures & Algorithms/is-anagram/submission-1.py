class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            if set(s)==set(t):
                for i in set(s):
                    if s.count(i) != t.count(i):
                        return False
                return True
            else:
                return False
        else:
            return False