class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key= lambda x :x[0])
        print(intervals)
        fin = [intervals[0]]
        for i in range(1, len(intervals)):
            last = fin.pop()
            curr = intervals[i]
            if last[1]>=curr[0]:
                new = [last[0], max(curr[1], last[1])]
                fin.append(new)
            else:
                fin.append(last)
                fin.append(curr)
        return fin