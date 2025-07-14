
def is_triangle(a, b, c):
# sum=[a,b,c]
# sum.sort()
# if sum[0]+sum[1]>sum[2]:
#      return True
# else:
#     return False
    return a + b > c and b + c > a and c + a > b
a,b,c=map(int,input().split())
print(is_triangle(a,b,c))