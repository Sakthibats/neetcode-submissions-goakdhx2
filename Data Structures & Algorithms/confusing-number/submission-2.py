class Solution:
    def confusingNumber(self, n: int) -> bool:
        st = str(n)
        fin = ""
        for ind in st:
            i = int(ind)
            if i in [2, 3, 4, 5, 7]:
                return False
            if i in [0, 1, 8]:
                fin = ind+fin
            if i in [6, 9]:
                fin = str([6, 9][i==6]) + fin
        # print(fin)
        if int(fin) == n:
            return False
        return True
        