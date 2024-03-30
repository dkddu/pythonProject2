# def to_binary(n,p):
#     if n >= p:
#         to_binary(n // p,p)
#     print(0 if n % p == 0 else n%p, end='')
# # Example usage:
# to_binary(129,8)
# def Fibonacci(n):
#     kb = [0]*n
#     kb[0] = 1
#     kb[1] = 1
#     for i in range(2,n):
#         kb[i]=kb[i-1]+kb[i-2]
#         print(kb)
# Fibonacci(5)
def forloop(n):
    if n==1:
        return 1
    return n+forloop(n-1)
print(forloop(5))