def remove_every_other(my_list):
    for i in my_list:
        m=my_list.index(i)
        print(i)
        if m%2==1:
                n=i
                #print(n)
                my_list.remove(n)
        #out.append(my_list[i+1])
    #return out
    return my_list
my_list1=[1,2,3,4,5,6,7,8,9,10]
print(remove_every_other(my_list1))