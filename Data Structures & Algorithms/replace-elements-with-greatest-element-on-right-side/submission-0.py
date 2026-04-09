class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        fin = [-1]
        maxval = arr[-1]
        for i in range(len(arr)-1,-1, -1):
            item = arr[i]
            maxval = max(maxval, item)
            fin.append(maxval)
        return fin[:-1][::-1]