# class Graph:
#     def __init__(self):
#         self.adj_list = {}
    
#     def AddVertex(self,vertex):
#         if vertex not in self.adj_list:
#             self.adj_list[vertex] = []
    
#     def AddEdge(self,vertex1,vertex2):
#         if vertex1 in self.adj_list and vertex2 in self.adj_list:
#             self.adj_list[vertex1].append([vertex2,1])
#             self.adj_list[vertex2].append([vertex1,1])
    
#     def PrintGraph(self):
#         for key,value in self.adj_list.items():
#             print(key,value)

# g = Graph()
# g.AddVertex(1)
# g.AddVertex(3)
# g.AddVertex(5)
# g.AddEdge(1,3)
# g.AddEdge(1,5)
# g.AddEdge(3,5)
# g.PrintGraph()


# Using Adjacency Matrix
# class Graph:
#     def __init__(self,vertices):
#         self.vertices = vertices
#         self.mat = [[0]*vertices for _ in range(vertices)]
    
#     def AddEdge(self,v1,v2):
#         self.mat[v1][v2] = 1
#         self.mat[v2][v1] = 1
    
#     def PrintGraph(self):
#         print(self.mat)
    
#     def Length(self):
#         return self.vertices

# g = Graph(5)
# g.AddEdge(0,1)
# g.AddEdge(0,2)
# g.AddEdge(1,3)
# g.AddEdge(2,4)
# g.PrintGraph()


# Depth First Search
# def DFS(graph,node,visited = set()):
#     print(node)
#     visited.append(node)
#     sm = 0
#     for child in graph[node]:
#         if child not in visited:
#             sm += DFS(graph,child,visited)
#     return sm+1

# graph = {
#     'A': ['B'],
#     'B': ['A', 'C'],
#     'C': ['B', 'D'],
#     'D': ['C', 'E'],
#     'E': ['D']
# }
# cnt = 0
# visited = []
# print(DFS(graph,'B',visited))



# graph = {
#     'A': ['B','C'],
#     'B': ['A','D'],
#     'C': ['A','E','F'],
#     'D': ['B','G'],
#     'E': ['C'],
#     'F': ['C'],
#     'G': ['D','H','I'],
#     'H': ['G'],
#     'I': ['G'],
# }
# distance = {
#     'A':None,
#     'B':None,
#     'C':None,
#     'D':None,
#     'E':None,
#     'F':None,
#     'G':None,
#     'H':None,
#     'I':None,
# }
# def sssp(graph,node,d,distance,parent):
#     distance[node] = d
#     for child in graph[node]:
#         if child != parent:
#             sssp(graph,child,distance[node]+1,distance,node)
# sssp(graph,'A',0,distance,None)
# for key,val in distance.items():
#     print(key,val)


# X = [[1,2],[2,3],[3,6],[6,5],[5,4],[4,1]]
# graph = {}
# visited = {}
# color = {}
# # print(visited)
# for i in range(1,7):
#     graph[i] = []
#     visited[i] = False
#     color[i] = None
# for u,v in X:
#     graph[u].append(v)
#     graph[v].append(u)
# # print(graph)

# def Bipartite(graph,node,visited,color,c):
#     visited[node] = True
#     color[node] = c
#     for child in graph[node]:
#         if not visited[child]:
#             temp = Bipartite(graph,child,visited,color,c^1)
#             if temp == False:
#                 return False
#         elif color[child] == color[node]:
#             return False
#     return True

# print(Bipartite(graph,1,visited,color,0))
# print(color)


# graph = {1:[2,3,5],
#          2:[1,3,4],
#          3:[1,2],
#          4:[2,5],
#          5:[1,4]
#          }
# visited = {i:False for i in range(1,6)}
# # print(graph,vertices)
# def dfs(graph,node,visited,parent):
#     visited[node] = True
#     for child in graph[node]:
#         if not visited[child]:
#             return dfs(graph,child,visited,node)
#         elif child != parent:
#             return True
#     return False
# print(dfs(graph,1,visited,-1))



# graph = {
#     1:[2,3,8],
#     2:[1,4,5,6],
#     3:[1,7],
#     4:[2],
#     5:[2],
#     6:[2],
#     7:[3],
#     8:[1]
# }
# timer = 1
# visited= {i:False for i in range(1,9)}
# intime = {i:None for i in range(1,9)}
# outtime = {i:None for i in range(1,9)}
# def dfs(graph,node,visited,intime,outtime):
#     global timer
#     intime[node] = timer
#     timer+=1
#     visited[node] = True
#     for child in graph[node]:
#         if not visited[child]:
#             dfs(graph,child,visited,intime,outtime)
#     outtime[node]= timer
#     timer+=1
# dfs(graph,1,visited,intime,outtime)
# print(intime)
# print(outtime)



# graph = {i:[] for i in range(1,10)}
# visited = {i:False for i in range(1,10)}
# graph[1].append(2)
# graph[1].append(6)
# graph[1].append(7)
# graph[1].append(8)
# graph[2].append(1)
# graph[2].append(3)
# graph[6].append(1)
# graph[3].append(2)
# graph[3].append(6)
# graph[3].append(4)
# graph[3].append(5)
# graph[4].append(3)
# graph[5].append(3)
# graph[6].append(3)
# graph[7].append(1)
# graph[7].append(9)
# graph[8].append(1)
# graph[8].append(9)
# graph[9].append(7)
# graph[9].append(8)

# def bfs(graph,visited):
#     q = []
#     ans = []
#     q.append(1)
#     visited[1] = True
#     while q:
#         temp = q.pop(0)
#         print(temp)
#         for child in graph[temp]:
#             if not visited[child]:
#                 q.append(child)
#                 visited[child] = True
#                 ans.append(child)

# bfs(graph,visited)




# pts = [[1,2],[1,3],[1,4],[1,6],[1,7],[1,8],[2,1],[2,3],[3,1],[3,4],[3,5],[3,6],[4,1],[4,3],[5,3],[6,1],[6,3],[7,1],[7,9],[8,1],[8,9],[9,7],[9,8]]
# graph = {}
# visited = {}
# distance = {}
# graph = {i:[] for i in range(1,10)}
# visited = {i:False for i in range(1,10)}
# distance = {i:None for i in range(1,10)}
# for u,v in pts:
#     graph[u].append(v)
#     graph[v].append(u)
# def bfs(graph,visited,distance):
#     q = []
#     q.append(1)
#     visited[1] = True
#     distance[1] = 0
#     while q:
#         temp = q.pop(0)
#         print(temp)
#         for child in graph[temp]:
#             if not visited[child]:
#                 q.append(child)
#                 visited[child] = True
#                 distance[child] = distance[temp] + 1
#     print(distance)
# bfs(graph,visited,distance)



# pts = [[1,2],[1,3],[1,7],[2,3],[4,1],[4,3],[5,3],[6,1],[6,3],[8,1],[9,7],[9,8]]
# visited = {}
# indegree = {}
# graph = {i:[] for i in range(1,10)}
# visited = {i:False for i in range(1,10)}
# indegree = {i:0 for i in range(1,10)}
# for u,v in pts:
#     graph[u].append(v)
#     indegree[v] += 1
# print(graph,indegree)

# def kahn(graph,visited,indegree):
#     q = []
#     for key in visited:
#         if indegree[key] == 0:
#             q.append(key)
#             visited[key] = True
#     while q:
#         temp = q.pop(0)
#         print(temp)
#         for child in graph[temp]:
#             indegree[child]-= 1
#             if indegree[child] == 0:
#                 q.append( child)
#                 visited[child] = True
# kahn(graph,visited,indegree)



# # Dfs on 2D grid
# def Isvalid(grid,visited,i,j):
#     row = len(grid)
#     col = len(grid[0])
#     if i<0 or j<0 or i>=row or j>=col or visited[i][j] == 1:
#         return False
#     return True
# def dfs(grid,visited,start):
#     i,j = start[0],start[1]
#     visited[i][j] = 1
#     print(grid[i][j])
#     if Isvalid(grid,visited,i-1,j):
#         dfs(grid,visited,[i-1,j])
#     if Isvalid(grid,visited,i,j+1):
#         dfs(grid,visited,[i,j+1])
#     if Isvalid(grid,visited,i+1,j):
#         dfs(grid,visited,[i+1,j])
#     if Isvalid(grid,visited,i,j-1):
#         dfs(grid,visited,[i,j-1])


# # Bfs on 2D grid
# def bfs(grid,visited,start):
#     q = []
#     q.append(start)
#     r,c = start[0],start[1]
#     visited[r][c] = 1
#     while q:
#         temp = q.pop(0)
#         x,y = temp[0],temp[1]
#         print(grid[x][y])
#         for a,b in [[-1,0],[0,1],[1,0],[0,-1]]:
#             if Isvalid(grid,visited,x+a,y+b):
#                 q.append([x+a,y+b])
#                 visited[x+a][y+b] = 1


# grid = [[3,1,5],[7,8,2],[14,11,9]]
# row = len(grid)
# col = len(grid[0])
# visited = [[0 for _ in range(col)] for _ in range(row)]
# # dfs(grid,visited,(1,1))
# bfs(grid,visited,(0,0))


# Disjoint sets
# pts = [[0,1],[1,2],[2,3],[4,5]]
# graph = {}
# for i in range(7):
#     graph[i] = -1
# for u,v in pts:
#     graph[u] = v

# # def find(graph,node):
# #     if graph[node] == -1:
# #         return node
# #     else:
# #         return find(graph,graph[node])

# def find(graph,node):
#     if graph[node] < 0:
#         return node
#     else:
#         temp = find(graph,graph[node])
#         graph[node] = temp
#         return temp
# def union(graph,a,b):
#     a = find(graph,a)
#     b = find(graph,b)
#     if a == b:
#         print("not possible")
#     else:
#         if graph[a] == graph[b]:
#             graph[b] = graph[b] + graph[a]
#             graph[a] = b
#         else:
#             if graph[a] < graph[b]:
#                 graph[a] = graph[a] + graph[b]
#                 graph[b] = a
#             else:
#                 graph[b] = graph[b] + graph[a]
#                 graph[a] = b
# print(graph)
# union(graph,0,4)
# print(graph)



# # Kruskal's Algorithm
# def find(graph,node):
#     if graph[node] < 0:
#         return node
#     else:
#         temp = find(graph,graph[node])
#         graph[node] = temp
#         return temp

# def union(graph,a,b,ans):
#     ta = a
#     tb = b
#     a = find(graph,a)
#     b = find(graph,b)
#     if a == b:
#         pass
#     else:
#         ans.append([ta,tb])
#         if graph[a] < graph[b]:
#             graph[a] = graph[a] + graph[b]
#             graph[b] = a
#         else:
#             graph[b] = graph[b] + graph[a]
#             graph[a] = b

# pts = [[1,2,1],[1,3,3],[2,6,4],[3,6,2],[3,4,1],[4,5,5],[5,6,6],[5,7,7]]
# graph = {}
# for i in range(1,8):
#     graph[i] = -1
# pts = sorted(pts,key = lambda pts: pts[2])
# ans = []
# for u,v,d in pts:
#     union(graph,u,v,ans)
# for item in ans:
#     print(item)        

# from heapq import *
# L = [4,9,7,1,8]
# # heapify(L)
# # or
# bag = []
# for item in L:
#     heappush(bag,item)
# # print(bag)
# # temp = heappop(bag)
# # print(bag)
# while bag:
#     print(heappop(bag))



# Prim's Algorithm
# from heapq import *
# def Prim(graph,distance,parent,visited,start):
#     bag = []
#     heappush(bag,[0,start])
#     distance[start] = 0
#     parent[start] = -1
#     while bag:
#         d,n = heappop(bag)
#         if not visited[n]:
#             visited[i] = 1
#             for cd,cn in graph[n]:
#                 if distance[cn] > cd and not visited[cn]:
#                     distance[cn] = cd
#                     parent[cn] = n
#                     heappush(bag,[cd,cn])
#     print(parent)
#     print(distance)


# pts = [[1,2,1],[2,3,4],[3,4,1],[4,5,2],[1,5,3],[2,5,2],[2,4,1]]
# graph = {}
# distance = {}
# visited = {}
# parent = {}
# for i in range(1,6):
#     graph[i] = []
#     parent[i] = None
#     distance[i] = float('inf')
#     visited[i] = False
 
# for u,v,d in pts:
#     graph[u].append([d,v])
#     graph[v].append([d,u])
# start = 1
# print(graph)
# Prim(graph,distance,parent,visited,start)


# Dijkstra Algorithm
# from heapq import *

# def Dijkstra(graph,distance,visited,start):
#     bag = []
#     distance[start] = 0
#     heappush(bag,[0,start])

#     while bag:
#         d,n = heappop(bag)
#         visited[n] = 1

#         for cd,cn in graph[n]:
#             if not visited[cn] and distance[n]+cd < distance[cn]:
#                 distance[cn] = distance[n] + cd
#                 heappush(bag,[distance[cn],cn])
#     print(distance)




# pts = [[1,3,2],[1,2,1],[2,3,1],[2,5,1],[3,4,2],[5,4,5]]
# graph = {}
# visited = {}
# distance = {}
# for i in range(1,6):
#     graph[i] = []
#     distance[i] = float('inf')
#     visited[i] = 0
# for u,v,d in pts:
#     graph[u].append([d,v])
#     graph[v].append([d,u])
# start = 1
# Dijkstra(graph,distance,visited,start)


# Floyd Warshell Algorithm
# pts = [[1,2,-1],[1,3,2],[2,3,3],[2,5,1],[3,5,2],[3,4,1],[4,5,2]]
# rows = 6
# cols = 6
# mat = []
# for _ in range(rows):
#     temp = []
#     for _ in range(cols):
#         temp.append(float('inf'))
#     mat.append(temp)

# for i in range(rows):
#     for j in range(cols):
#         if i == j:
#             mat[i][j] = 0

# for u,v,d in pts:
#     mat[u][v] = d

# for k in range(1,6):
#     for i in range(1,rows):
#         for j in range(1,cols):
#             if i == j or i == k or j == k:
#                 pass
#             else:
#                 if  mat[i][k] + mat[k][j] < mat[i][j]:
#                     mat[i][j] = mat[i][k] + mat[k][j]
# print(mat)


# Bellman Ford Algorithm
# pts = [[1,2,2],[1,3,1],[2,3,-2],[2,4,2],[3,5,-1],[4,5,1]]
# n = 5
# distance = {}
# for i in range(1,6):
#     distance[i] = 10**8 +1
# distance[1] = 0
# for _ in range(n-1):
#     for u,v,d in pts:
#         if distance[u] + d < distance[v] :
#             distance[v] = distance[u] + d
# print(distance)

