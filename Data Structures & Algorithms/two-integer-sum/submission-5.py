class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        pseudo code
        - for each element in list # outer loop to get element at index i
            - for each element in list # inner loop to get element at index j
                - if element_at_i + element_at_j == target and index_i =! index_j
                    - return [index_i, index_j]
        """
        print (nums)
        for i,first in enumerate(nums):
            print(i,first)
            for j, second in enumerate(nums):
                if first+second==target and i<j:
                    return [i,j]
          