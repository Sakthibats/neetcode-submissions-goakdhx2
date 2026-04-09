class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        fin = set()
        candidates.sort()
        def help(prev, arr, summ):
            if summ==target:
                fin.add(tuple(arr))
            elif summ>target:
                pass
            else:
                for i in range(prev+1, len(candidates)):
                    help(i, arr+[candidates[i]], summ+candidates[i])
        help(-1,[], 0)
        return [list(i) for i in fin]