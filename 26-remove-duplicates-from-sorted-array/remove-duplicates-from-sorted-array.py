class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        temp = []
        k=0
        for num in nums:
            if num not in list(d.keys()):
                d[num]=1
                temp.append(num)
                k+=1
        
        temp.extend([0]*(len(nums)-k))
        nums[:] = temp

        return k
        