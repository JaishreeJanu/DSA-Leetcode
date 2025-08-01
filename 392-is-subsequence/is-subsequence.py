class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        j = 0
        for elem in s:
            while j<len(t) and elem != t[j]:
                j+=1

            if j==len(t): return False
            j+=1
            

        return True