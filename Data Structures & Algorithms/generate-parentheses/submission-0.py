class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        fin = []
        start = ""
        listt = []
        def helper(string, opener, closer, listted):
            if closer==n:
                fin.append(string)
            else:
                if listted:
                    curr = listted.pop()
                    helper(string+")", opener, closer+1, listted)
                    listted.append(curr)
                    if opener<n:
                        helper(string+"(", opener+1, closer, listted+["("])
                else:
                    helper(string+"(",opener+1, closer, listted+["("])
        helper(start, 0, 0, listt)
        print(fin)
        return fin
        
        