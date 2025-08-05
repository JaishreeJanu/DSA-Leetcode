class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        threesum_triplets = set()

        for i in range(0,n-2):
            j = i+1
            k = n-1
            while j<k:
                curr_sum = nums[i]+nums[j]+nums[k]
                if curr_sum == 0:    
                    threesum_triplets.add((nums[i],nums[j],nums[k]))


                    j += 1
                    k -= 1
                elif curr_sum<0:
                    j += 1
                else:
                    k -= 1

        return [list(triplet) for triplet in threesum_triplets]
        