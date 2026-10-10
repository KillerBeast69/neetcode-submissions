class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dict1 = {}

        for i in range(len(s)):

            if s[i] in dict1:
                if dict1[s[i]] != t[i]:
                    return False

            dict1[s[i]] = t[i]

        return True