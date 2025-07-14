def high_and_low(numbers):
    lst1=numbers.split()
    # print(lst1)
    lst=[]
    for i in lst1:
        # print(i)
        a=int(i)
        lst.append(a)
    lst.sort()
    # print(lst)
    n=str(lst[0])
    lst.reverse()
    m=str(lst[0])
    s=m+" "+n
    return s
numbers="8 3 -5 42 -1 0 0 -9 4 7 4 -4"
print(high_and_low(numbers))
# print(high_and_low("1 2 3 4 5")) # return "5 1"
# print(high_and_low("1 2 -3 4 5")) # return "5 -3"
# print(high_and_low("1 9 3 4 -5"))