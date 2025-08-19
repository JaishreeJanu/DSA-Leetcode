class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up,down = 0,len(matrix)-1
        
        while up<=down:
            mid_index = (up+down)//2
            lookup_mat = matrix[mid_index]
            if target > lookup_mat[-1]:
                up = mid_index+1
            elif target < lookup_mat[0]:
                down = mid_index-1
            else:
                left,right = 0,len(lookup_mat)-1
            
                while left<=right:
                    mid_index = (right+left)//2

                    if lookup_mat[mid_index] == target:
                        return True
                    elif lookup_mat[mid_index] > target:
                        right = mid_index-1
                    else:
                        left = mid_index+1
                return False

        return False
        