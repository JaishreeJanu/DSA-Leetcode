class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_uniq_count = 0
        uniq_hash = {}

        i = 0
        for j, elem in enumerate(s):
            if elem in uniq_hash and uniq_hash[elem] >= i:
                    max_uniq_count = max(max_uniq_count, j-i)
                    i = uniq_hash[elem]+1
            uniq_hash[elem] = j
                    
               
                
        max_uniq_count = max(max_uniq_count, len(s)-i)
        
        return max_uniq_count
        