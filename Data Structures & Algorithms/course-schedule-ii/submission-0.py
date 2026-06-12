class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visitedCourses, cycleSet = set(), set()       # respectively for output visited and cycle visited
        res = []
        prerequisitesMap = {i : [] for i in range(numCourses)}        # course -> [prerequisites]
        for course, prerequisite in prerequisites:
            prerequisitesMap[course].append(prerequisite)
        
        def dfs(course) -> bool:       # can course be completed or not
            if course in cycleSet: return False
            if course in visitedCourses: return True
                        
            cycleSet.add(course)
            for prerequisiteCourse in prerequisitesMap[course]:
                if not dfs(prerequisiteCourse): return False
    
            cycleSet.remove(course)       # Allow traversal from different path
            visitedCourses.add(course)    # Clear prerequisites so we don't have to do dfs on all prerequisites again
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course): return []
        return res