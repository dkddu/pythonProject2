apple=list(map(int,input().split()))
height=int(input())
n=0
for i in range(0,9):
    if apple[i]<=height+30:
        n+=1
print(n)