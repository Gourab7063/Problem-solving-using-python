def descending_order(num):
    # Bust a move right here
    s=str(num)
    lst=[]
    for i in s:
        lst.append(int(i))
    lst.sort()
    lst.reverse()
    su=0
    for i in lst:
        su=su*10+i
    return su
num=int(input())
print(descending_order(num))