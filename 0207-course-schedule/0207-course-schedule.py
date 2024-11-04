class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph= defaultdict(list)
        ind = [0 for _ in range(numCourses)]

        for i,j in prerequisites:
            ind[i] += 1
            graph[j].append(i)
        
        print(graph, ind)

        q = []
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)
        
        ans = []
        while q:
            node = q.pop(0)
            ans.append(node)
            print(node)
            
            for child in graph[node]:
                ind[child] -= 1
                if ind[child] == 0:
                    q.append(child)
                
        return numCourses == len(ans)
        

