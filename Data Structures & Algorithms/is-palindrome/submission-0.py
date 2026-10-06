class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l1 = []
        for ch in s:
            if ch.isalnum():
                l1.append(ch)
        if l1 == l1[::-1]:
            return True
        return False