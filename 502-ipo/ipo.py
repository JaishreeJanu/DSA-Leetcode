class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # First need a paired list of Profits and capital, sorted by capital

        projects = sorted(zip(capital, profits))
        n = len(projects)
        i = 0

        # second a max-heap of profits
        max_profit_heap = []

        for _ in range(k):

            while i<n and w >= projects[i][0]:
                heapq.heappush(max_profit_heap, -projects[i][1])
                i += 1

            if not max_profit_heap: return w

            w += -heapq.heappop(max_profit_heap)

        return w