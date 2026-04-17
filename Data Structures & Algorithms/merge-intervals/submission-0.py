class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        fin = []
        start, end = intervals[0]
        point = 1
        while point<len(intervals):
            currstart, currend = intervals[point]
            if currstart>end:
                fin.append([start, end])
                start, end = currstart, currend
            elif currstart<=end:
                end = max(end, currend)
            point +=1
        fin.append([start, end])
        return fin
#merge
# curr end in between start and stop of next

#dont merge and continue
                

