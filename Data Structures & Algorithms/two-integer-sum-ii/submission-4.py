class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = numbers
        l = 0
        r = len(a)-1
        while l<r:
            q = target - a[l]
            if q == a[r]:
                list_1 = [l+1,r+1]
                return list_1
            elif q < a[r]:
                r = r - 1
            else: 
                l = l + 1
                