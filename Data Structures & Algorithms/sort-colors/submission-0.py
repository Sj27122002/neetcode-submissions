class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        l = 0
        r = len(nums) - 1
        a = nums
        
        def swap(i,j):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        
        while(i-1<r):
            if a[i] == 0:
                swap(i,l)
                l = l + 1
            
            elif a[i] == 2:
                swap(i,r)
                r = r - 1
                i = i - 1

            i = i + 1        