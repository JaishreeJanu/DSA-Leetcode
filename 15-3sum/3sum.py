class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        threesum_triplets = []
        triplets_hash = {}

        for i in range(0,n-2):
            j = i+1
            k = n-1
            while j<k:
                curr_sum = nums[i]+nums[j]+nums[k]
                if curr_sum == 0:
                    if (nums[i],nums[j],nums[k]) not in triplets_hash:
                        triplets_hash[(nums[i],nums[j],nums[k])] = 1
                        threesum_triplets.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                elif curr_sum<0:
                    j += 1
                else:
                    k -= 1

        return threesum_triplets
        