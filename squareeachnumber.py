num=int(input())
# s=0
# s1=0
# while num!=0:
#     r=num%10
#     s=s*10+r
#     num=num//10
# while s!=0:
#     r1=s%10
#     if r1<4:
#         s1=s1*10+(r1)**2
#     else:
#         s1=s1*100+(r1)**2
#     s=s//10
# print(s1)
nums=str(num)
s=0
for i in nums:
    if num<4:
        s1=s1*10+int(i)**2
    else:
        s=s*100+int(i)**2
print(s)

    