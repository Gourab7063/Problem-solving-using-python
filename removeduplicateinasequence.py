def unique_in_order(sequence):
    lst=[]
    n=None
    for i in sequence:
        if i!=n:
             lst.append(i)
        else:
            pass
        n=i
    return lst
sequence=[0,2,2,3,3]
print(unique_in_order(sequence))