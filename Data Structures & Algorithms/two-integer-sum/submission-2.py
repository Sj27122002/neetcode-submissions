class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = len(nums)   
        for i in range(k):
            q = target - nums[i]
            for j in range(i+1,k):
                if q == nums[j]:
                    return [i,j]