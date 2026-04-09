class Solution:
    def canFinish(self, numCourses: int, preq: List[List[int]]) -> bool:
        dic = {i:[] for i in range(numCourses)}
        for i, j in preq:
            dic[i] = dic.get(i, []) + [j]
        
        visitset = set()

        def dfs(course):
            if course in visitset:
                return False
            if dic[course] == []:
                return True
            visitset.add(course)
            for pre in dic[course]:
                if not dfs(pre):
                    return False
            visitset.remove(course)
            dic[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True