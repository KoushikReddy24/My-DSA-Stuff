from heapq import *
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        ans = defaultdict(int)
        for i,j,k in roads:
            g[i].append([k,j])
            g[j].append([k,i])
        dist = [float('inf')]*n
        ways = [0]*n
        ways[0] = 1
        def dijkstra(node):
            dist[node] = 0
            bag = []
            heappush(bag,[0,node])
            while bag:
                d,node = heappop(bag)
                for cd,cn in g[node]:
                    nd = cd + d
                    if nd == dist[cn]:
                        ways[cn] += ways[node]
                    if dist[cn] > nd:
                        dist[cn] = cd + dist[node]
                        heappush(bag,[dist[cn],cn])
                        ways[cn] = ways[node]
        dijkstra(0)
        MOD = 10**9+7
        return ways[n-1]%MOD

        # visited = []
        # def dfs(node,x,ttl):
        #     if ttl == x and node == n-1:
        #         return 1
        #     if ttl < x:
        #         temp = 0
        #         for cd,cn in g[node]:
        #             if cn not in visited:
        #                 temp += dfs(cn,x, ttl+cd)
        #         return temp
        #     else:
        #         return 0
        
        # return dfs(0,x,0)
