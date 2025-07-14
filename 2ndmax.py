import numpy as np
def getSecondLargest(arr):
        arr=np.sort(arr)
        n=len(arr)
        # print(n)
        arr=np.flip(arr)
        m=arr[0]
        # print(arr)
        if n<2:
            return (-1)
        for i in arr:
            #print(i)
            if m==i:
                c=-1
            elif m>i:
                c=i
                break
        if c==m:
            return (-1)
        else:
            return(c)
arr = np.array([10,10,10])
p=getSecondLargest(arr)
print(p)           