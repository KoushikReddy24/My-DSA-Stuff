from collections import OrderedDict
import numpy as np
n = int(input())
S = []
for _ in range(n):
    S.append(input())
A = list(set(S))
D = {}
for i in range(n):
    if(S[i] not in D):
        D[S[i]] = i
    else:
        D[S[i]] = i
B = []

K = list(D.keys())
V = list(D.values())
Sorted_index = np.argsort(V)
Sorted_dict = {K[i]: V[i] for i in Sorted_index}

print(Sorted_dict)
Sorted_Keys = list(Sorted_dict.keys())
print(Sorted_Keys)
for i in Sorted_Keys:
    print(i[-2],end="")
    print(i[-1],end="")
print()
# print(V)
# V.sort(reverse=True)
# print(V)
# for i in V:
#     print(i)
#     x = list(D.keys())[V.index(i)]
#     B.append(x)
# print(B)
# for i in B:
# 	print(i[-2],end="")
# 	print(i[-1],end="")
# print()



 
 
