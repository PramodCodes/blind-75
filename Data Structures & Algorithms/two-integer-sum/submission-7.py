class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,iv in enumerate(nums):
            for j,sv in enumerate(nums):
                if i<j and iv+sv==target:
                    return [i,j]