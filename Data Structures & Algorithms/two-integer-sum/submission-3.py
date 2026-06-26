class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print (nums)
        for fe in nums:
            for se in nums:
                print (nums.index(fe),nums.index(se))
                if fe+se == target and nums.index(fe)!=nums.index(se):
                    return [nums.index(fe),nums.index(se)]