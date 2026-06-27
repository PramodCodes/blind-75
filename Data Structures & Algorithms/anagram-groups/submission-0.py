class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
    
        visited = [False]*len(strs)
        for oi,ov in enumerate(strs):
            # 1. Skip this word if it was already caught in a previous anagram group
            if visited[oi]:
                continue # this will skip the next statements for current iteration and increments counter

            temp_res = []
            temp_res.append(ov)
            s_ov=sorted(ov)
            visited[oi] = True

            for ci in range(oi+1, len(strs)):
                s_ce = sorted(strs[ci])
                # if s_ov == s_ce and not visited[ci]:
                if s_ov == s_ce and not visited[ci]:
                    visited[ci] = True
                    temp_res.append(strs[ci])
            result.append(temp_res)
        return result