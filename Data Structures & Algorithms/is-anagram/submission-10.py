class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Since expressions evaluate to True or False, you can just return the comparison directly
        return len(s) == len(t) and sorted(s) == sorted(t)
