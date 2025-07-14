def first_non_consecutive(arr):
    m=arr[0]
    c=True
    for i in arr:
        if m!=i:
            c=i
            break
        m=m+1
    if c==True:
        return None
    else:
        return c
   
arr=[-3,-2,0,1]
print(first_non_consecutive(arr))