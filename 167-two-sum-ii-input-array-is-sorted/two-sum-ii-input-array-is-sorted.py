class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        numb_hash = {}

        for ind,number in enumerate(numbers):
            search_num = target - number
            if search_num in numb_hash.keys():
                return (numb_hash[search_num]+1, ind+1)
            if number not in numb_hash.keys():
                numb_hash[number] = ind

        


        