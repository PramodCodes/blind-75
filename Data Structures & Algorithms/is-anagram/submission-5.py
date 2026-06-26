class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print (s)
        print (t)
        if len(s) == len(t):
            print("length of s and t matchs")
            for counter in s:
                source=list(s)
                target=list(t)
                print(source.sort(),target.sort())
                print(source,target)

            return True