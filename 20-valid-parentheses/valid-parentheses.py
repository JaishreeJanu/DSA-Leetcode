class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairs = {')': '(', ']': '[', '}': '{'}
        
        for elem in s:
            if elem in ['[', '(', '{']:
                stack.append(elem)
            elif elem in [']', ')', '}']:
                if not stack or bracket_pairs[elem] != stack.pop():
                    return False


            
        return not stack

        