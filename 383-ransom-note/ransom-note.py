class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maga_hash = {}

        for elem in magazine:
            if elem not in maga_hash:
                maga_hash[elem] = 1
            else:
                maga_hash[elem] += 1

        for elem in ransomNote:
            if elem not in maga_hash:
                return False
            else:
                if maga_hash[elem] > 0:
                    maga_hash[elem] -= 1
                else:
                    return False      


        return True