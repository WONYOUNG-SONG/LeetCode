class Solution:
    def isValid(self, s: str) -> bool:
        dic = dict(('()', '{}', '[]'))
        stack = []
        
        for c in s:
            if c in '({[':
                stack.append(c)
            elif len(stack) == 0 or c != dic[stack.pop()]:
                return False
        return not stack