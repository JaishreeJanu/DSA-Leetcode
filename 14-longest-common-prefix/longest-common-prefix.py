class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        i = 0
        long_prefix = ""

        while True:
            if len(strs[0]) <= i: return long_prefix
            this_char = strs[0][i]
            for j in range(len(strs)):
                if len(strs[j]) <= i: return long_prefix
                if strs[j][i] != this_char: return long_prefix

            long_prefix += this_char
            i += 1


        