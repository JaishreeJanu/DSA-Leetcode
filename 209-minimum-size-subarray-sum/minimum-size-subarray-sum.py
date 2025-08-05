class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target: return 0
        i = 0
        min_len = float("inf")
        n = len(nums)
        curr_sum = 0
        for j in range(n):
            curr_sum += nums[j]
            while curr_sum >= target:
                min_len = min(min_len, j-i+1)
                curr_sum -= nums[i]
                i += 1

        return min_len

        
        