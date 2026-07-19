class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisitesmap = {course : [] for course in range(numCourses)}
        for course1, course2 in prerequisites:
            prerequisitesmap[course1].append(course2)
        
        vis = set()
        def dfs(course):
            if course in vis: return False
            if prerequisitesmap[course] == []: return True
            vis.add(course)
            for prerequisite in prerequisitesmap[course]:
                if not dfs(prerequisite): return False
            vis.remove(course)
            prerequisitesmap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True