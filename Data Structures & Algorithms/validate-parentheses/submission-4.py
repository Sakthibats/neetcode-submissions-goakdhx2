class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_dict = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in close_dict:
                if stack and close_dict[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False