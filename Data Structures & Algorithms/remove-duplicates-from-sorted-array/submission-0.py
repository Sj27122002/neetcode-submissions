class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        list_1 = []
        count = 0
        i = 0
        while i < len(nums):
            nums[count] = nums[i]
            count = count + 1
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j = j + 1
            i = j
            
        return count