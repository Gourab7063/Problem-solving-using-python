
list=[1, 2, 'a', 'b']
list1=[]
for i in list:
    if type(i)==int:
        list1.append(i)
print(list1)