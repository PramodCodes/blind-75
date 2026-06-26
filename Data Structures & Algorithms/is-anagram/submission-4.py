class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print (s)
        print (t)
        if len(s) == len(t):
            print("length of s and t matchs")
            for source in s:
                source=s.split()
                target=t.split()
                print(source,target.sort())

            return True