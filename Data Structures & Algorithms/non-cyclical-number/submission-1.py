class Solution:
    def isHappy(self, n: int) -> bool:
        sett = set()
        sett.add(1)
        val = self.summ(n)
        while val not in sett:
            sett.add(val)
            val = self.summ(val)
            print(val, sett)
        return val==1
            

    def summ(self, n):
        summation = 0
        for i in str(n):
            summation += int(i)**2
        return summation

        