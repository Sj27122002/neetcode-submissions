class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        l = set()
        i = 0
        def sums(a,b,c):
            return nums[a] + nums[b] + nums[c]
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j<k:
                if sums(i,j,k) == 0:
                    l.add(tuple([nums[i],nums[j],nums[k]]))
                    j += 1
                    k -= 1
                elif sums(i,j,k) > 0:
                    k = k-1
                elif sums(i,j,k) < 0:
                    j = j+1    
        return[list(x) for x in l]        
                
                
            
            
            