     for i in range(len(list)-1):
            n=list.index(list[i])
            for j in range(len(list)-n-1):
                    list[i],list[i+1]=list[i+1],list[i]
                    print(list)