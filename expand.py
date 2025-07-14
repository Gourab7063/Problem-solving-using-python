#    12 --> "10 + 2"
#    45 --> "40 + 5"
# 70304 --> "70000 + 300 + 4"

def expanded_form(num):
    
    lst=[]
    while num!=0:
        n=len(str(num))-1
        a=num//10**n
        b=num%10**n
        # lst=[a*10**n,b]
        lst.append(a*10**n)
        num=b
        n=n-1
    x=" + ".join(map(str,lst))
    return x
    

num=int(input())
print(expanded_form(num))