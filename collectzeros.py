
# n=list.count(0)
# for i in range(n):
#     list.remove(0)
#     list.append(0)
# print(list)
# a=0

# for b in range(len(list)):
#     for i in range(len(list)-1):
#         n=list.index(list[i])
#         for j in range(len(list)-n-1):
#             if a==list[i]:
#                 list[i],list[i+1]=list[i+1],list[i]
# print(list)
def pushZerosToEnd(arr):
    count = 0  # Position to place the next non-zero element

    # Move non-zero elements forward
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    # Fill remaining positions with zeros
    while count < len(arr):
        arr[count] = 0
        count += 1

    return arr
list=[1,0, 2, 0, 1, 2, 3, 0, 1]
print(pushZerosToEnd(list))