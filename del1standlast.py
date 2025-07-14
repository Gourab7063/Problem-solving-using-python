def remove_char(s):
    #your code here
    lst=[]
    for i in s:
        lst.append(i)
    n=len(lst)-2

    print(lst[n])
    lst.pop(0)
    lst.pop(n)
    x=''.join(lst)
    return x
s=input()
print(remove_char(s))