class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        threesum_triplets = []

        for i in range(0,n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j<k:
                curr_sum = nums[i]+nums[j]+nums[k]
                if curr_sum == 0:    
                    threesum_triplets.append([nums[i],nums[j],nums[k]])

                    while j<k and nums[j]==nums[j+1]:
                        j += 1
                    while j<k and nums[k]==nums[k-1]:
                        k -= 1

                    j += 1
                    k -= 1
                elif curr_sum<0:
                    j += 1
                else:
                    k -= 1

        return threesum_triplets
        