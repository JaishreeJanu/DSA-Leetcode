class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i=1
        curr = nums[0]
        flag=False
        while i<len(nums):
            if nums[i]==curr:
                if not flag:
                    flag=True
                    i+=1
                else:
                    nums.pop(i)
            else:
                curr = nums[i]
                i += 1
                flag=False



        