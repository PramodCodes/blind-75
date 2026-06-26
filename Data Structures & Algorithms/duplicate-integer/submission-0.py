class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(sorted(nums)) != len(set(nums))