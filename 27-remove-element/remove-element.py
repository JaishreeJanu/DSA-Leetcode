class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        k=0
        n = len(nums)
        for num in nums:
            if num!=val:
                temp.append(num)
                k += 1
        
        temp.extend([0]*(n-k))

        nums[:] = temp
        return k