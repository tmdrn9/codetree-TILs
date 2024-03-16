n,m=map(int,input().split())
d=[]
for i in range(n):
    d.append(input())
for j in range(m):
    g=input()
    if g.isdigit():
        print(d[int(g)-1])
    else:
        print(d.index(g)+1)