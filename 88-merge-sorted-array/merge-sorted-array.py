class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m==0:
            nums1[:]=nums2
            return
        if n==0:
            return
        
        merged = []
        j=0
        i=0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                merged.append(nums1[i])
                i += 1
            elif nums1[i]>nums2[j]:
                merged.append(nums2[j])
                j += 1
            else:
                merged.extend([nums1[i],nums2[j]])
                i+=1
                j+=1

        if i==m:
            merged.extend(nums2[j:])
        else:
            merged.extend(nums1[i:m])

        nums1[:] = merged

        return
        