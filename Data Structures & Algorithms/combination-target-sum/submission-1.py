class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        fin = set()
        def help(listt, summ):
            if summ==target:
                fin.add(tuple(sorted(listt)))
            elif summ>target:
                pass
            else:
                for i in nums:
                    help(listt+[i], summ+i)
        help([], 0)
        return [list(i) for i in fin]

                