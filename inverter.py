# def invert(lst):
#     for i in lst:
#         lst.append(-1*lst[i])
#     return lst
lst=[1,2,3,4,5]
for i in range(len(lst)):
    lst[i]=-1*lst[i]
print(lst)