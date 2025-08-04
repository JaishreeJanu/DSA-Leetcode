class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        numb_hash = {}

        for ind,number in enumerate(numbers):
            search_num = target - number
            if search_num in numb_hash:
                return [numb_hash[search_num]+1, ind+1]
            
            numb_hash[number] = ind

        


        