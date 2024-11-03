class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        gp = defaultdict(list)
        for i,j in edges:
            gp[i].append(j)
            gp[j].append(i)
        
        LN = []
        for key in gp.keys():
            if len(gp[key]) == 1:
                LN.append(key)
        
        while len(gp) > 2:
            NL = []
            for leaf in LN:
                x = gp[leaf][0]
                gp.pop(leaf)
                gp[x].remove(leaf)
                if len(gp[x]) == 1:
                    NL.append(x)
            
            LN = NL
        L = []
        for key in gp.keys():
            L.append(key)
        return L