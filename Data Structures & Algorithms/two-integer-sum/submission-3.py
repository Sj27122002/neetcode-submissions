class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            q = target - n
            if q in seen:
                return [seen[q],i]
            seen[n] = i
        