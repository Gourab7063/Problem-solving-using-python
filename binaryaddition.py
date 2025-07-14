def add_binary(a,b):
    #your code here
    c=a+b
    if c<=1:
        return str(c)
    else:
        s=0
        i=0
        while c!=0:
            r=c%2
            c=c//2
            s=s+(r*10**i)
            i=i+1
        return str(s)
a=int(input("Enter a number"))
b=int(input("Enter a number"))
print(add_binary(a,b))