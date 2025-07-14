def tribonacci(signature, n):
    a,b,c=signature[0],signature[1],signature[2]
    if n==0:
        return []
    elif n==1:
        return [a]
    elif n==2:
        return[a,b]
    elif n==3:
        return[a,b,c]
    else:
        for i in range(n-3):
            d=a+b+c
            signature.append(d)
            a,b,c=b,c,d
    return signature
print(tribonacci([1, 1, 1], 10))
print(tribonacci([0, 0, 1], 10))
print(tribonacci([0, 1, 1], 10))
print(tribonacci([1, 0, 0], 10))
print(tribonacci([0, 0, 0], 10))
print(tribonacci([1, 2, 3], 10))
print(tribonacci([3, 2, 1], 10))
print(tribonacci([1, 1, 1], 1))
print(tribonacci([300, 200, 100], 0))
print(tribonacci([0.5, 0.5, 0.5], 30))
