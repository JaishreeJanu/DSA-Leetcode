class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        
        while left<=right:
            mid_index = (right+left)//2

            if nums[mid_index] == target:
                return nums.index(target)
            elif nums[mid_index] > target:
                right = mid_index-1
            else:
                left = mid_index+1

        return left
                