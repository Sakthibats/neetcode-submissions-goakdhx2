class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        fin = []
        def help(dig, string):
            nonlocal fin
            if len(dig)==0:
                fin.append(string)
            else:
                curr = dig[0]
                for i in dic[curr]:
                    help(dig[1:], string+i)
        if digits:
            help(digits, "")
        return fin

                
        