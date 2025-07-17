class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        length = m+n
        mid_ind = length//2
        merged_list = []
        i=0
        j=0
        k=0

        while (i<m and j<n):
            if nums1[i] < nums2[j]:
                merged_list.append(nums1[i])
                i += 1
                k += 1
            elif nums2[j] < nums1[i]:
                merged_list.append(nums2[j])
                j += 1
                k += 1
            else:
                merged_list.extend([nums1[i], nums2[j]])
                i += 1
                j += 1
                k += 2

            if k == mid_ind+1:
                if length%2 == 0:
                    sum = merged_list[k-1] + merged_list[k-2]
                    
                    return (sum) / 2
                else:
                    return merged_list[k-1]

        if i==m:
            merged_list.extend(nums2[j:])
        
        else:
            merged_list.extend(nums1[i:])
        
        
        if length%2 == 0:
            sum = merged_list[mid_ind-1] + merged_list[mid_ind]
            
            return (sum) / 2
        else:
            return merged_list[mid_ind]
        