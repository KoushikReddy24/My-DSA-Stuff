# #iterative approach
# def BinSearch(arr,low,high,x):
#     while(low <= high):
#         mid = (low+high)//2

#         if(arr[mid]==x):
#             return mid
#         elif(arr[mid]>x):
#             high = mid-1
#         else:
#             low = mid+1
#     return -1

# arr = [2,3,4,7,8,9,10]
# x = 9
# y = BinSearch(arr,0,len(arr)-1,x)
# if(y == -1):
#     print(f"Element {x} is not found in the array {arr}")
# else:
#     print(f"Element {x} is found at {y+1} in the array {arr}")



#recursive approach
def BinSearch(arr,low,high,x):
    if(low <= high):
        mid = (low+high)//2
        if(arr[mid] == x):
            return mid
        elif arr[mid]>x:
            return BinSearch(arr,low,mid-1,x)
        else:
            return BinSearch(arr,mid+1,high,x)
    return -1

arr = [2,3,4,7,8,9,10]
x = 9
y = BinSearch(arr,0,len(arr)-1,x)
if(y == -1):
    print(f"Element {x} is not found in the array {arr}")
else:
    print(f"Element {x} is found at {y+1} in the array {arr}")
