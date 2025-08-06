class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
    
        longest_c = 0
        for num in nums:
            if num-1 in nums:
                continue
            elem = num+1
            c = 1
            while elem in nums:
                c += 1
                elem += 1
            
            longest_c = max(longest_c, c)

        return longest_c

        