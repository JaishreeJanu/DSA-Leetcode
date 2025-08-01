class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)
        
        i=1

        while i < len(ratings):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
            i += 1
        
        i = len(ratings)-2
        while i>=0:
            if ratings[i] > ratings[i+1] and candies[i]<= candies[i+1]:
                candies[i] = candies[i+1] + 1

            i -= 1



        return sum(candies)



        