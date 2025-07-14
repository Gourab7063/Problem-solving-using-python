def longest(a1, a2):
    # your code
    x=set()
    lst=[]
    z=a1+a2
    for i in z:
        x.add(i)
    for i in x:
        lst.append(i)
    lst.sort()
    s=''.join(lst)# to join any list items
    return s

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

a1="xyaabbbccccdefww"
a2="xxxxyyyyabklmopq"
print(longest(a1, a2))
