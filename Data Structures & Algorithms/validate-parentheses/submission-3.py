class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i not in dic:
                stack.append(i)
            else:
                if stack and (stack[-1])==dic[i]:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
                
        