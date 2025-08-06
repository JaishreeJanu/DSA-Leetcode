class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        from collections import Counter
        hash_counter = Counter(nums)
        longest_c = 0
        for i in range(len(nums)):
            elem = nums[i]
            if elem-1 in hash_counter:
                continue
            elem += 1
            c = 1
            while elem in hash_counter:
                c += 1
                elem += 1
            else:
                longest_c = max(longest_c, c)

        return longest_c

        