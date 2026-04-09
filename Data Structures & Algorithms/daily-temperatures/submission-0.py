class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        arr = []
        fin = [0]*len(temps)

        for i, t in enumerate(temps):
            while arr and t>arr[-1][0]:
                st, si = arr.pop()
                fin[si] = i-si
            arr.append((t, i))
        return fin
        