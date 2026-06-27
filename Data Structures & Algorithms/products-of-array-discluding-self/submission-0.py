class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        i = 0
        j = 0
        product = 1
        product_0 = 1
        if  0 in nums:
            num_0 = nums.copy()
            num_0.remove(0)
            for i in range(len(num_0)):
                product_0 = num_0[i]*product_0
        for i in range(len(nums)):
            product = nums[i]*product
        for j in range(len(nums)):
            if nums[j] == 0:
                out_cont = product_0
            else:
                out_cont = product//nums[j]
            out.append(out_cont)
        return out