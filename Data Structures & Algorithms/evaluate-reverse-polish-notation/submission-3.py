class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        ops = ["+", "-", "*", "/"]
        for ind, item in enumerate(tokens):
            if item not in ops:
                arr.append(int(item))
            else:
                sec = arr.pop()
                fir = arr.pop()
                if item=="+":
                    arr.append(fir + sec) 
                elif item=="-":
                    arr.append(fir - sec) 
                elif item=="*":
                    arr.append(fir * sec) 
                elif item=="/":
                    arr.append(int(fir / sec)) 
        return arr[-1]
