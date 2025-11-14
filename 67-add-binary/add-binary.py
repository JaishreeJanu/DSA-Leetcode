class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        res = []
        i,j = len(a)-1, len(b)-1
        carry = 0
        while i>=0 or j>=0:
            bitA = int(a[i]) if i>=0 else 0
            bitB = int(b[j]) if j>=0 else 0

            curr_sum = bitA+bitB+carry
            
            res.append(str(curr_sum%2))
            carry = curr_sum//2

            i -= 1
            j -= 1

        if carry: res.append(str(carry))
        return "".join(reversed(res))


        