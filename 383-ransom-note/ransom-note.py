class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        r,m = Counter(ransomNote), Counter(magazine)

        return all(m[c]>=r[c] for c in r)