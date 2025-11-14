class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        if not nums1 or not nums2 or k == 0:
            return []

        min_heap = []  # (sum, i, j)
        res = []

        # Initialize heap with pairs (nums1[i], nums2[0])
        # Only need up to k entries
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        # Extract k smallest pairs
        while min_heap and len(res) < k:
            s, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])

            # Push next pair in the row: (nums1[i], nums2[j+1])
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))

        return res



            
            


        