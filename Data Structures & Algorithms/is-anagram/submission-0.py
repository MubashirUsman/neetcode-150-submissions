class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first solution: check length -> convert to list -> 
        # sort lists -> check equality
        # second solution: find each char count in both -> check 
        # if each char count is equal
        if len(s) != len(t):
            return False
        ls = sorted(list(s))
        lt = sorted(list(t))
        if ls != lt:
            return False
        return True
