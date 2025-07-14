def likes(names):
    # your code here
    if len(names)==0:
        return "no one likes this"
    elif len(names)<4:
        for i in names:
            print(i)
        return i
names=[] 
likes(names)