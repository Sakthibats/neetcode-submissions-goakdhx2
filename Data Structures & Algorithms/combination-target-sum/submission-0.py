class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        finset = set()
        fin = []
        def helper(summ, comb):
            if summ==target:
                new = tuple(sorted(comb))
                if new not in finset:
                    finset.add(new)
                    fin.append(comb)
            elif summ<target:
                for i in nums:
                    helper(summ+i, comb+[i])
        helper(0, [])
        return fin